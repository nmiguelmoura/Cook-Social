# -*- coding: utf-8 -*-

from google.appengine.ext import db

class DBQueryRecipes:
    """Class that performs queries in RecipesDBModel. Allows to search for
    recipes based on recipe id, recipe user, top voted and new publications."""

    def __init__(self):
        pass

    def search_recipes_by_id(self, id):
        # Query recipes based on recipe id.
        recipes = db.GqlQuery("SELECT * FROM RecipesDBModel WHERE __key__ = KEY('RecipesDBModel', " + str(id) + ")")
        for r in recipes:
            return r

    def search_new_recipes(self, limit, offset):
        # Query recipes based on creation date.
        # Limits results to given number.
        recipes = db.GqlQuery("SELECT * FROM RecipesDBModel ORDER BY created DESC LIMIT %s OFFSET %s" % (limit, offset))
        return recipes

    def search_top_recipes(self, limit, offset):
        # Query recipes based on points.
        # Limits results to given number.
        recipes = db.GqlQuery("SELECT * FROM RecipesDBModel ORDER BY points DESC LIMIT %s" % (limit, offset))
        return recipes

    def search_recipes_by_user_id(self, id):
        # Query recipes based on author id.
        recipes = db.GqlQuery("SELECT * FROM RecipesDBModel WHERE user_id='%s' ORDER BY created DESC" % id)
        return recipes
