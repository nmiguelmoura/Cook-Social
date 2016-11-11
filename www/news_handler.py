import handler
import prefabs.db_query_recipes

class NewsHandler(handler.Handler):
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()

    def get(self):
        limit = 10
        recipes = self.query_recipes.search_new_recipes(limit)
        self.render("news.html", recipes=recipes)
