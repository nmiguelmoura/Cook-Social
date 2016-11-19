# -*- coding: utf-8 -*-

import handler
import prefabs.cookie_handler
import prefabs.db_query_recipes

class DeleteRecipeHandler(handler.Handler):
    """Class that handles recipe deletion."""

    cookies = prefabs.cookie_handler.CookieHandler()
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()

    def recipe_valid_access(self):
        #
        # Get posted data.
        user_id = self.get_user()
        recipe_id = self.request.get("id")

        if recipe_id:
            # If there is a recipe id, search for it in db.
            recipe = self.query_recipes.search_recipes_by_id(recipe_id)

            if recipe and recipe.user_id == user_id:
                # If recipe exists in db, and recipe author id matches user id,
                # return it.
                return recipe
            else:
                # If recipe does not exist in db or recipe author is different
                # from the one that is logged in, redirect to error
                # message page.
                self.redirect("messagetouser?type=permission_error")
        else:
            # If there is no recipe id, redirect to message page.
            self.redirect("/messagetouser")

    def get_user(self):
        # Return user id stored in cookies.
        return self.cookies.get_loginfo_cookie(self)

    def post(self):
        # Check if recipe exists and if recipe author is the same that
        # is logged in.
        recipe = self.recipe_valid_access()
        if recipe:
            # If data pass validation, get recipe title to show on message page
            # and delete it from db.
            title = recipe.title
            recipe.delete()
            self.render("delete_recipe.html", title=title)
