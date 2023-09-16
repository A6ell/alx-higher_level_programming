#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object by sorting by id and using .first()
    first_state = session.query(State).order_by(State.id).first()

    # If the table states is empty, print "Nothing"
    if first_state is None:
        print("Nothing")
    else:
        # Print the first State object
        print("{}: {}".format(first_state.id, first_state.name))

    # Close the session
    session.close()
