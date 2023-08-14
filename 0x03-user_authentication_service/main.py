#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User
import logging


from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
# Set the desired logging level for other SQLAlchemy categories
logging.getLogger('sqlalchemy.pool').setLevel(logging.WARNING)
logging.getLogger('sqlalchemy.dialects').setLevel(logging.INFO)
# Add more category loggers and set their levels as needed


my_db = DB()

email = 'test@test.com'
hashed_password = "hashedPwd"

user = my_db.add_user(email, hashed_password)
print(user.id)

try:
    my_db.update_user(user.id, hashed_password='NewPwd')
    print("Password updated")
except ValueError:
    print("Error")

