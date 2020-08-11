#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref=state, cascade="all, delete-orphan")
    if HBNB_TYPE_STORAGE == "file":
        @property
        def cities(self):
            """ Get value for cities """
            cityList = []
            for i in list(models.storage.all(City).values()):
                if i.state_id == self.id:
                    cityList.append(i)
            return cityList
