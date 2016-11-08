from google.appengine.ext import db
from google.appengine.api import images


class RecipesDBModel(db.Model):
    user_id = db.StringProperty(required=True)
    title = db.StringProperty(required=True)
    prep_time = db.IntegerProperty(required=True)
    points = db.IntegerProperty(required=True)
    comments = db.ListProperty(str)
    ingredients = db.ListProperty(str, required=True)
    steps = db.ListProperty(str, required=True)
    image = db.BlobProperty()
    created = db.DateTimeProperty(auto_now_add=True)
