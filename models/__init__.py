#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
if HBNB_TYPE_STORAGE == "db":
    import db_storage
    storage = db_storage()
    storage.reload()
elif HBNB_TYPE_STORAGE == "file":
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
