#!/usr/bin/python3
"""Containes the class definition of a City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State



class City(Base):
    """City class that inherits from Base"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
