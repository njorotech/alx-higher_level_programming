#!/usr/bin/python3
"""changes the name of a State object from the
database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

if __name__ == '__main__':
    user = argv[1]
    paswd = argv[2]
    db = argv[3]

    db_url = f'mysql+mysqldb://{user}:{paswd}@localhost:3306/{db}'
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    updated_state = session.query(State).filter_by(id=2).first()
    updated_state.name = "New Mexico"
    session.add(updated_state)
    session.commit()
