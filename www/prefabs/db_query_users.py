# -*- coding: utf-8 -*-

from google.appengine.ext import db

class DBQueryUsers:
    """Class that performs queries in UsersDBModel. Allows to search for
    users based on user id, username and email."""

    def __init__(self):
        pass

    def search_user(self, username):
        # Query users based on username.
        user = db.GqlQuery("SELECT * FROM UsersDBModel WHERE username='%s'" % username)
        for u in user:
            return u

    def search_user_by_id(self, id):
        # Query users based on user id.
        user = db.GqlQuery("SELECT * FROM UsersDBModel WHERE __key__ = KEY('UsersDBModel', " + str(id) + ")")
        for u in user:
            return u

    def search_email(self, email):
        # Query users based on email.
        user = db.GqlQuery("SELECT * FROM UsersDBModel WHERE email='%s'" % email)
        for u in user:
            return u
