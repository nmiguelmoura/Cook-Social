from google.appengine.ext import db

import handler


class ImageRecipeHandler(handler.Handler):
    def get(self):
        image_key = self.request.get("img_id")
        recipe = self.search_recipe(image_key)

        if recipe.image:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(recipe.image)
        else:
            self.response.out.write('')

    def search_recipe(self, id):
        recipe = db.GqlQuery("SELECT * FROM RecipesDBModel WHERE __key__ = KEY('RecipesDBModel', " + id + ")")
        for r in recipe:
            return r
