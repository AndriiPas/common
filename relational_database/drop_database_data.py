import psycopg2

<<<<<<< HEAD
from config import DATABASE
from db_utils import clear_tables, drop_tables
=======
from relational_database.config import DATABASE
from relational_database.db_utils import clear_tables, drop_tables
>>>>>>> upstream/master

if __name__ == "__main__":
    con = psycopg2.connect(**DATABASE)
    with con.cursor() as cursor:
        try:
            clear_tables(cursor)
            drop_tables(cursor)
            con.commit()
        finally:
            if con:
                con.close()
