import handler
import prefabs.cookie_handler
import prefabs.db_query_recipes

class DeleteRecipeHandler(handler.Handler):
    cookies = prefabs.cookie_handler.CookieHandler()
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()

    def recipe_valid_access(self):
        user_id = self.get_user()
        recipe_id = self.request.get("id")

        print user_id
        print recipe_id

        if recipe_id:
            recipe = self.query_recipes.search_recipes_by_id(recipe_id)

            if recipe and recipe.user_id == user_id:
                return recipe
            else:
                self.redirect("messagetouser?type=permission_error")
        else:
            self.redirect("/messagetouser")

    def get_user(self):
        return self.cookies.get_loginfo_cookie(self)

    def post(self):
        recipe = self.recipe_valid_access()
        if recipe:
            title = recipe.title
            recipe.delete()
            self.render("delete_recipe.html", title=title)
