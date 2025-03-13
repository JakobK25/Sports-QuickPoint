import time
import random
from datetime import datetime
from db.database import insert_score

# Define the team names
team_names = ["HOLD1", "HOLD2", "HOLD3", "HOLD4"]

def generate_scores(db, connection):
    for i in range(10):
        score = random.randint(1, 5)
        team_name = random.choice(team_names)
        timestamp = datetime.now()
        
        # Insert score record using the db module function
        insert_score(db, timestamp, team_name, score)
        connection.commit()
        
        print(f"Data inserted: {timestamp} | Team: {team_name} | Goals: {score}")
        
        # Random delay between insertions
        delay = random.randint(1, 5)
        time.sleep(delay)
