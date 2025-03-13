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

for team in team_names:
    db.execute("SELECT scores_goals FROM public.scores WHERE scores_team_name = %s", (team,))
    goals = db.fetchall()
    print(f"Team {team} has {len(goals)} goals")


print(len(record), "rows returned")

connection.close()





