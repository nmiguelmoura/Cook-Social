import handler
import prefabs.cookie_handler
import prefabs.db_query_recipes
import prefabs.db_query_users

class KitchenHandler(handler.Handler):
    cookies = prefabs.cookie_handler.CookieHandler()
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()
    query_users = prefabs.db_query_users.DBQueryUsers()

    def get(self):
        user_id = self.cookies.get_loginfo_cookie(self)

        if user_id:
            user = self.query_users.search_user_by_id(user_id)
            if user:
                username = user.username
                limit = 10
                recipes = self.query_recipes.search_new_recipes(limit)
                self.render("kitchen.html", user_id=user_id, username=username, recipes=recipes)
            else:
                self.redirect("/login")
        else:
            self.redirect("/login")
