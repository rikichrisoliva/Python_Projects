import psycopg2
from postgresconfig import config

def connect():
    connection = None   # a None type, an object that indicates no value, don't return anything

    try:
        params = config()
        #print(params)
        #print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)     # kwargs or double asterisks keyword arguments work with dictionaries. to extract everything inside the params inside those two parenthesis.
        crsr = connection.cursor()
        #print('PostgreSQL database version: ')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close() # the cursor and the connection is the communication way between the Python file and the database
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)        # way of handling any errors that might occur in the above code block
    finally:
        if connection is not None:      # after this assignment connection = psycopg2.connect(**params), connection is NOT None anymore
            connection.close()
            #print('Database connection terminated.')

if __name__ == "__main__":
    # print(__name__)   output is __main__
    connect()

