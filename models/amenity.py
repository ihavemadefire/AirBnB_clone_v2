#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class Amenity(BaseModel, Base):
    """ Class amenity inherits base and basemodel """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity')
