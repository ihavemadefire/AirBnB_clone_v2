#!/usr/bin/python3
"""This is the DB file storage engine"""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.state import State
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.place import Place
from models.city import City
from models.review import Review
from models.user import User
import sys
import os

HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST")
HBNH_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")


class DBStorage:
    """ class DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        """ public instance methods """
        self.__engine = create_engine(
                                      'mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST, HBNH_MYSQL_DB),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        # if HBNB_ENV == 'test':
        # LOOK INTO THIS, DROP ALL TABLES?

    def all(self, cls=None):
        """ query current database """
        if cls is None:
            result = self.__session.query(User).all()
            result.extend(self.__session.query(State).all())
            result.extend(self.__session.query(City).all())
            result.extend(self.__session.query(Amenity).all())
            result.extend(self.__session.query(Place).all())
            result.extend(self.__session.query(Review).all())

        else:
            if type(cls) == str:
                cls = eval(cls)
            result = self.__session.query(cls)
        ret = {}
        for i in result:
            key = i.__class__.__name__ + '.' + i.id
            value = i
            ret[key] = value
        return ret

    def new(self, obj):
        """ add the obj to the current database """
        self.__session.add(obj)

    def save(self):
        """ commit all changes to db storage """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from current db storage """
        if obj is None:
            return
        else:
            self.__session.delete(obj)

    def reload(self):
        """ reload db storage """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """calls close on the session"""
        self.__session.close()
