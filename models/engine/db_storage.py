
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from models.state import State
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
import sys


class DBStorage:
    """ class DBStorage """
    __engine = None
    __session = None

    def__init__(self):
        """ public instance methods """
