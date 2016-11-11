import handler
import prefabs.cookie_handler
import prefabs.db_query_recipes

class MainHandler(handler.Handler):
    cookies = prefabs.cookie_handler.CookieHandler()
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()

    def get(self):
        user_id = self.cookies.get_loginfo_cookie(self)
        if user_id:
            self.redirect("/kitchen")
        else:
            limit = 10
            recipes = self.query_recipes.search_new_recipes(limit)
            self.render("main.html", recipes=recipes)
