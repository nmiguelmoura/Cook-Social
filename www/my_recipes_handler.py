import handler
import prefabs.db_query_recipes
import prefabs.db_query_users
import prefabs.cookie_handler

class MyRecipesHandler(handler.Handler):
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()
    query_users = prefabs.db_query_users.DBQueryUsers()
    cookies = prefabs.cookie_handler.CookieHandler()

    def render_content(self, user_id):
        user = self.query_users.search_user_by_id(user_id)
        if user:
            username = user.username
            recipes = self.query_recipes.search_recipes_by_user_id(user_id)
            no_recipes_message = "" if recipes.count() > 0 else "This cook doesn't published any recipes yet!"
            self.render("my_recipes.html", username=username, recipes=recipes,
                        no_recipes_message=no_recipes_message)
        else:
            self.redirect("messagetouser")

    def get(self):
        user_id = None
        get_id = self.request.get("id")
        if get_id:
            user_id = get_id
        else:
            user_id = self.cookies.get_loginfo_cookie(self)
            if not user_id:
                self.redirect("login")
                return

        self.render_content(user_id)
