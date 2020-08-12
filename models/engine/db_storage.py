
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
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
        self.__engine = create_engine(
                                      'mysql+mysqldb://{}:{}@localhost/{}'.
                                      format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST, HBNH_MYSQL_DB)
                                      pool_pre_pring=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        # if HBNB_ENV == 'test':
        # LOOK INTO THIS, DROP ALL TABLES?

    def all(self, cls=None):
        """ query current database """
        if cls is None:
            result = self.__session.query()
        else:
            result = self__session.query(cls)
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
            class = obj.class
            id = obj.id
            result = self.__session.query().filter({obj.id})
            self.__session.delete(result)

    def reload(self):
        """ reload db storage """
        pass
