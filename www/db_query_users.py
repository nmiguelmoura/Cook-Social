from google.appengine.ext import db

class DBQueryUsers:
    def __init__(self):
        pass

    def search_user(self, username):
        user = db.GqlQuery("SELECT * FROM UsersDBModel WHERE username='%s'" % username)
        for u in user:
            return u

    def search_user_by_id(self, id):
        user = db.GqlQuery("SELECT * FROM UsersDBModel WHERE __key__ = KEY('UsersDBModel', " + str(id) + ")")
        for u in user:
            return u

    def search_email(self, email):
        user = db.GqlQuery("SELECT * FROM UsersDBModel WHERE email='%s'" % email)
        for u in user:
            return u

    # def get_user_id(self, username):
    #     user = db.GqlQuery("SELECT * FROM UsersDBModel WHERE username='%s'" % username)
    #     for u in user:
    #         print "####"
    #         print u
    #         print "####"
    #         return u