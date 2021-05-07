import psycopg2, time

# Connect to an existing database
conn = psycopg2.connect("dbname=postgres user=postgres password=password host=129.114.27.48 port=5431")
print('connection establiched')
time.sleep(2)
# Open a cursor to perform database operations
cur = conn.cursor()
cur.execute("SELECT * FROM t1;")
# try:
#     cur.execute("SELECT *;")
# except psycopg2.Error as e:
#     print (e.pgerror)

# Make the changes to the database persistent
conn.commit()

cur.close()
conn.close()