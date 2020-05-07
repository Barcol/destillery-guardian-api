import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def prepare_database_structure():
    conn = create_connection("database.db")
    print(conn)


if __name__ == '__main__':
    prepare_database_structure()
