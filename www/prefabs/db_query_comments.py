from google.appengine.ext import db

class DBQueryComments:
    def __init__(self):
        pass

    def search_comments_by_id(self, id):
        comments = db.GqlQuery("SELECT * FROM CommentsDBModel WHERE __key__ = KEY('CommentsDBModel', " + str(id) + ")")
        for c in comments:
            return c

    def search_comments_by_recipe_id(self, recipe_id):
        comments = db.GqlQuery("SELECT * FROM CommentsDBModel WHERE recipe_id='%s' ORDER BY created DESC" % recipe_id)
        return comments
