import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

cur = None
conn = None

def create_table():
    try:
        with psycopg.connect(
            host = os.getenv('HOSTNAME'),
            dbname = os.getenv('DATABASE_NAME'),
            user = os.getenv('USERNAME'),
            password = os.getenv('PASSWORD_TEXT'),
            port = os.getenv('PORT_ID')) as conn:

            with conn.cursor() as cur:
                table = os.getenv('TABLE_NAME')
                create_script = f''' CREATE TABLE IF NOT EXISTS {table} (
                                        id BIGSERIAL PRIMARY KEY,
                                        source VARCHAR(255),
                                        title TEXT NOT NULL,
                                        url TEXT NOT NULL UNIQUE,
                                        published TIMESTAMP,
                                        content TEXT,
                                        collected_at TIMESTAMP NOT NULL)'''
                cur.execute(create_script)


    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == "__main__":
    create_table()
