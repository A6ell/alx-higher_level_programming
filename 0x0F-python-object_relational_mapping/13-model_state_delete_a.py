#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: {} <mysql_username> <mysql_password> <database_name>".format(
                sys.argv[0]))
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

    # Query the database to find all State objects with a name containing 'a'
    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    # Close the session
    session.close()
