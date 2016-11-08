from google.appengine.ext import db


class CommentsDBModel(db.Model):
    user_id = db.StringProperty(required=True)
    recipe_id = db.StringProperty(required=True)
    comment = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
