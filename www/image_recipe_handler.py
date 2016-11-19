# -*- coding: utf-8 -*-

from google.appengine.ext import db

import handler


class ImageRecipeHandler(handler.Handler):
    """Class to be called from a page when need to display a recipe image
    stored in db."""

    def get(self):
        # Get image key.
        image_key = self.request.get("img_id")

        # Get recipe entity with given id.
        recipe = self.search_recipe(image_key)

        if recipe.image:
            # Write image if exists in recipe entity.
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(recipe.image)
        else:
            # Write nothing if image does not exist.
            self.response.out.write('')

    def search_recipe(self, id):
        # Return recipe entity with given id.
        recipe = db.GqlQuery(
            "SELECT * FROM RecipesDBModel WHERE __key__ = KEY('RecipesDBModel', " + id + ")")
        for r in recipe:
            return r
