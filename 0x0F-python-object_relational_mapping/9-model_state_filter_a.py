#!/usr/bin/python3
"""lists all State objects that contain letter a from the
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

    result = session.query(State).filter(
            State.name.like("%a%")).order_by(State.id)
    for state in result:
        print(f'{state.id}: {state.name}')
