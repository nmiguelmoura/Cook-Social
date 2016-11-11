import handler
import prefabs.db_query_recipes

class TopHandler(handler.Handler):
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()

    def get(self):
        limit = 10
        recipes = self.query_recipes.search_top_recipes(limit)
        self.render("top.html", recipes=recipes)