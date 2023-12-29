#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
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

    result = session.query(State.name, City.id, City.name).join(State).all()
    for row in result:
        print(f'{row[0]}: ({row[1]}) {row[2]}')
