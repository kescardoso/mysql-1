import os
import pymysql

# Get username from Gitpod Workspace
username = os.getenv('GP_USER')

# Connect to the databas
connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM Friends WHERE name in ('bob','jim')")
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
