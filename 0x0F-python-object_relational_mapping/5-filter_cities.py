#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <database> <state_name>".format(
                sys.argv[0]))
        sys.exit(1)

    # Extract the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

        # Execute the SQL query to fetch cities of the specified state
        query = "SELECT cities.name FROM cities \
                 INNER JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all the results
        cities = cursor.fetchall()

        # Extract city names from the result and join them
        city_names = [city[0] for city in cities]
        cities_str = ', '.join(city_names)

        # Print the results
        print(cities_str)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
