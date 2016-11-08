from google.appengine.ext import db

class DBQueryRecipes:
    def __init__(self):
        pass

    def search_recipes_by_id(self, id):
        recipes = db.GqlQuery("SELECT * FROM RecipesDBModel WHERE __key__ = KEY('RecipesDBModel', " + str(id) + ")")
        for r in recipes:
            return r
