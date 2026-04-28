from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
    	host=os.getenv("DB_HOST", "db"),
    	database=os.getenv("DB_NAME", "mydb"),
    	user=os.getenv("DB_USER", "user"),
    	password=os.getenv("DB_PASSWORD", "pass")
    )
    return conn

@app.route("/")
def home():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Hello DevOps! DB: {db_version}"
    except Exception as e:
        return f"DB connection error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
