#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Execute the SQL query to fetch cities along with their corresponding
        # state names
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                 INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
        cursor.execute(query)

        # Fetch all the results
        cities = cursor.fetchall()

        # Print the results
        for city in cities:
            print(city)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
