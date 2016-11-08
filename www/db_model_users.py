from google.appengine.ext import db


class UsersDBModel(db.Model):
    username = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    pointed = db.ListProperty(str)
    comments = db.ListProperty(str)
    created = db.DateTimeProperty(auto_now_add=True)
