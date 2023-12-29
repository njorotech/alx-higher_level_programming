#!/usr/bin/python3
"""prints the State object with the name pass as argument
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

if __name__ == '__main__':
    user = argv[1]
    paswd = argv[2]
    db = argv[3]
    name = argv[4]

    db_url = f'mysql+mysqldb://{user}:{paswd}@localhost:3306/{db}'
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(
            State.name == name).first()
    if result is None:
        print('Not found')
    else:
        print(f'{result.id}')
