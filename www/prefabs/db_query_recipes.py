from google.appengine.ext import db

class DBQueryRecipes:
    def __init__(self):
        pass

    def search_recipes_by_id(self, id):
        recipes = db.GqlQuery("SELECT * FROM RecipesDBModel WHERE __key__ = KEY('RecipesDBModel', " + str(id) + ")")
        for r in recipes:
            return r

    def search_new_recipes(self, limit):
        recipes = db.GqlQuery("SELECT * FROM RecipesDBModel ORDER BY created DESC LIMIT %s" % limit)
        return recipes

    def search_top_recipes(self, limit):
        recipes = db.GqlQuery("SELECT * FROM RecipesDBModel ORDER BY points DESC LIMIT %s" % limit)
        return recipes

    def search_recipes_by_user_id(self, id):
        recipes = db.GqlQuery("SELECT * FROM RecipesDBModel WHERE user_id='%s' ORDER BY created DESC" % id)
        return recipes
