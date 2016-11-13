from google.appengine.ext import db


class DBQueryComments:
    """Class that performs queries in CommentsDBModel. Allows to search for
    comments based on comment id and recipe id."""

    def __init__(self):
        pass

    def search_comments_by_id(self, id):
        # Query comments based on comment id.
        comments = db.GqlQuery(
            "SELECT * FROM CommentsDBModel WHERE __key__ = KEY('CommentsDBModel', " + str(
                id) + ")")
        for c in comments:
            return c

    def search_comments_by_recipe_id(self, recipe_id):
        # Query comments based on recipe id.
        comments = db.GqlQuery(
            "SELECT * FROM CommentsDBModel WHERE recipe_id='%s' ORDER BY created DESC" % recipe_id)
        return comments
