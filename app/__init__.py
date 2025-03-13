import time
from datetime import datetime
from .config import load_config
from db.database import get_connection, get_recent_scores, get_team_goals, get_team_with_most_goals
from .score import generate_scores

def run_app():
    # Load environment configuration
    config = load_config()
    
    # Wait for PostgreSQL to initialize
    print("Waiting for PostgreSQL to initialize...")
    time.sleep(5)
    
    # Connect to the database
    connection, db = get_connection(config)
    
    # Display start time
    startTime = datetime.now()
    print("Start running at:", startTime)
    
    # Insert random score entries
    generate_scores(db, connection)
    
    # Retrieve and print recent records
    record = get_recent_scores(db)
    
    team_names = ["HOLD1", "HOLD2", "HOLD3", "HOLD4"]
    for team in team_names:
        goals = get_team_goals(db, team)
        print(f"Team {team} has {len(goals)} goals")
    
    # Determine and display the team with the most goals
    team_most_goals = get_team_with_most_goals(db)
    if team_most_goals:
        print(f"Team with most goals: {team_most_goals[0][0]}")
    
    print(len(record), "rows returned")
    connection.close()
