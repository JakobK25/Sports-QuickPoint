import psycopg2

def get_connection(config):
    try:
        connection = psycopg2.connect(
            database=config["POSTGRES_DB"],
            user=config["POSTGRES_USER"], 
            password=config["POSTGRES_PASSWORD"],
            host="sqp_postgres_db",
            port=5432
        )
        print("Connected to the database")
    except:
        # Fallback to localhost if service name doesn't work
        connection = psycopg2.connect(
            database=config["POSTGRES_DB"],
            user=config["POSTGRES_USER"],
            password=config["POSTGRES_PASSWORD"],
            host="127.0.0.1",
            port=5432
        )
        print("Connected to the localhost database")
    return connection, connection.cursor()

def get_recent_scores(db):
    db.execute("SELECT * FROM public.scores ORDER BY scores_time DESC LIMIT 10")
    return db.fetchall()

def get_team_goals(db, team):
    db.execute("SELECT scores_goals FROM public.scores WHERE scores_team_name = %s", (team,))
    return db.fetchall()

def get_team_with_most_goals(db):
    db.execute("SELECT scores_team_name, COUNT(scores_team_name) FROM public.scores GROUP BY scores_team_name ORDER BY COUNT(scores_team_name) DESC LIMIT 1")
    return db.fetchall()

def insert_score(db, timestamp, team_name, score):
    db.execute(
        "INSERT INTO public.scores (scores_time, scores_team_name, scores_goals) VALUES (%s, %s, %s)", 
        (timestamp, team_name, str(score))
    )

def get_match_scores(db, team1, team2):
    db.execute(
        "SELECT scores_goals FROM public.scores WHERE scores_team_name = %s OR scores_team_name = %s", 
        (team1, team2)
    )
    return db.fetchall()

def get_event(db, team_name):
    db.execute("SELECT * FROM public.scores WHERE scores_team_name = %s", (team_name,))
    return db.fetchall()