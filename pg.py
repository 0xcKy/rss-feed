#file used to connect to postgresql, called on rss.py
#still needs configuration file containing sensetive data as hostname, database, username, password and port. Will be added later.

import psycopg

#use config file for the sensetive data
hostname = 'localhost'
database = 'db_name'
username = 'postgres'
pwd = 'password'
port_id = 'port'
cur = None
conn = None

def pg_db_write(i):
    pg_connect(i)

def pg_connect(i):
    try:
        with psycopg.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id) as conn:

            with conn.cursor() as cur:

                create_script = ''' CREATE TABLE IF NOT EXISTS news (
                                        id BIGSERIAL PRIMARY KEY,
                                        source VARCHAR(255),
                                        title TEXT NOT NULL,
                                        url TEXT NOT NULL,
                                        published TIMESTAMP,
                                        content TEXT,
                                        collected_at TIMESTAMP NOT NULL)'''
                cur.execute(create_script)

                insert_script = 'INSERT INTO news (source, title, url, published, content, collected_at) VALUES (%s, %s, %s, %s, %s, %s)'
                insert_value = ((i["source"]), (i["title"]), (i["url"]), (i["published"]), (i["content"]), (i["collected_at"]))
                cur.execute(insert_script, insert_value)

                cur.execute('SELECT * FROM news')
                print(cur.fetchall())

    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    pg_connect()
