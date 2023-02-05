import psycopg2
import psycopg2.extras  # use this kind of cursor if you want to reference by the name of the column (and not referencing by the index, 0 by the id and 1 by the name)

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
# conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port="1111")
# by the cursor method on the connection allows to execute SQL statement
cur = conn.cursor()

# cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")
# have to commit on the connection every time you run a statement, every change the database you have to commit when you're done.
# cur.execute("INSERT INTO student (name) VALUES(%s)", ("Rambert",))    # %s is a placeholder, this execute will add anything that you supply as a sequence as a second argument into the %s
# if you have three %s inside the statement, then you need a sequence of three things
# use a Tuple for this example

cur.execute("SELECT * FROM student;")
print(cur.fetchall())  # to view the output of the SELECT statement above
cur.execute("SELECT * FROM student WHERE id = %s;", (2,))
print(cur.fetchone())  # to view the output of the SELECT statement above


cur2 = conn.cursor(
    cursor_factory=psycopg2.extras.DictCursor
)  # use this kind of cursor if you want to reference by the name of the column
cur2.execute("SELECT * FROM student;")
print(cur2.fetchall())  # to view the output of the SELECT statement above
cur2.execute("SELECT * FROM student WHERE id = %s;", (2,))
print(cur2.fetchone()["name"])  # to view the output of the SELECT statement above

conn.commit()

cur.close()  # similar to the connection, you have to close the cursor when done.
conn.close()  # have to close the connection in the end
print(
    "################################################################################################"
)
####################################################################################################
# use WITH statement, once the with statement has finished executing, it's going to close the cursor automatically, no need to write the close on the cursor
# you can not get around closing the connection, but you can get around writing the commit
# when run the with statement on the connection, once the with statement has finished executing, it is going to commit for you automatically
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

with conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur3:
        # cur3.execute("INSERT INTO student (name) VALUES(%s)", ("David",))
        cur3.execute("SELECT * FROM student;")
        print(cur3.fetchall())

conn.close()
