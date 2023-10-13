import psycopg2


# Paramètres de connexion
conn = psycopg2.connect(
    "dbname='postgres_db' user='admin' host='localhost' password='secret' port='5433'")
cur = conn.cursor()
