#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
# from models.__init__ import storage
# from models.engine.db_storage import DBStorage
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    amenities = relationship('Amenity',
                             secondary='place_amenity', viewonly=False)

    @property
    def reviews(self):
        """Get reviews for filestorage"""
        reviews = []
        for review in list(models.storage.all(Review).values()):
            if review.place_id == self.id:
                reviews.append(review)
            return reviews

    @property
    def amenities(self):
        """ Get amenity values """
        amenities = []
        for amenity in list(models.storage.all(Amenity).values()):
            if amenity.amenity_ids == self.id:
                amenities.append(amenity)
            return amenities

    @amenities.setter
    def amenities(self, value):
        """ Sets the amenity value """
        self.amenity_ids.append(value)
