from .db import db
from flask_mongoengine import mongoengine
# from mongoengine import *
import datetime

class User(db.Document):
    user_id = db.IntField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField()
    chat_id = db.IntField(required=True, unique=True)
    # name = db.StringField(required=True, unique=True)
    # casts = db.ListField(db.StringField(), required=True)
    # genres = db.ListField(db.StringField(), required=True)

class Task(db.Document):
    created = db.DateTimeField(default=datetime.datetime.utcnow)
    title = db.StringField(max_length=120, required=True)
    description = db.StringField(max_length=255)
    due_date = db.DateTimeField(default=datetime.datetime.utcnow)
    notification = db.DateTimeField(default=datetime.datetime.utcnow)
    status = db.StringField(default='undone')
    user_id = db.IntField(required=True)
