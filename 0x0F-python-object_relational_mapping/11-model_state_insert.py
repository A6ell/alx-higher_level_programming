#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage = (
            "Usage: {} <mysql_username> <mysql_password> <database_name>"
            .format(sys.argv[0])
        )
print(usage)
sys.exit(1)


mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# Create a connection to the database
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}' .format(
        mysql_username,
        mysql_password,
        database_name),
    pool_pre_ping=True)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a new State object
new_state = State(name="Louisiana")

# Add the new State object to the session and commit it to the database
session.add(new_state)
session.commit()

# Print the new state's id
print(new_state.id)

# Close the session
session.close()
