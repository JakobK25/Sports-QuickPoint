import psycopg2

def get_connection(config):
    connection = psycopg2.connect(
        database=config["POSTGRES_DB"],
        user="postgres",
        password=config["POSTGRES_PASSWORD"],
        host="127.0.0.1",
        port=5432
    )
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
