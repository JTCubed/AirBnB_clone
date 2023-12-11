#!/usr/bin/python3
"""Storage variable"""
from models.engine.file_storage import FileStorage
from models.user import User


storage = FileStorage()

storage.reload()
from models.base_model import BaseModel
