# Install required libraries


# Import libraries

import os
import time
import random
import pygame
import pyfirmata
from datetime import datetime
import psycopg2
from dotenv import load_dotenv
from pathlib import Path

# Load the environment variables
env_path = Path('.') / '.env'
load_dotenv(env_path)

# Get environment variables
db_name = os.getenv("POSTGRES_DB")
db_password = os.getenv("POSTGRES_PASSWORD")

# Connect to the database using environment variables
connection = psycopg2.connect(
    database=db_name,
    user="postgres", 
    password=db_password, 
    host="127.0.0.1", 
    port=5432
)
db = connection.cursor()

## Setup time
startTime = datetime.now()
print("Start running at: ", startTime)

## Generate random data and time
team_names = ["HOLD1", "HOLD2", "HOLD3", "HOLD4"]

for i in range(10):
    score = random.randint(1, 5)
    team_name = random.choice(team_names)
    timestamp = datetime.now()

    db.execute(
        "INSERT INTO public.scores (scores_time, scores_team_name, scores_goals) VALUES (%s, %s, %s)", 
        (timestamp, team_name, str(score))
    )
    connection.commit()
    
    print(f"Data inserted: {timestamp} | Team: {team_name} | Goals: {score}")

    delay = random.randint(1, 5)
    time.sleep(delay)

## Read data from database
db.execute("SELECT * FROM public.scores ORDER BY scores_time DESC LIMIT 10")
record = db.fetchall()

# Print teams goals
for team in team_names:
    db.execute("SELECT scores_goals FROM public.scores WHERE scores_team_name = %s", (team,))
    goals = db.fetchall()
    print(f"Team {team} has {len(goals)} goals")

# Print team with most goals
db.execute("SELECT scores_team_name, COUNT(scores_team_name) FROM public.scores GROUP BY scores_team_name ORDER BY COUNT(scores_team_name) DESC LIMIT 1")
team_most_goals = db.fetchall()
print(f"Team with most goals: {team_most_goals[0][0]}")

print(len(record), "rows returned")

connection.close()





