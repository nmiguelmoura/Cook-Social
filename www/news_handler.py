import handler
import prefabs.db_query_recipes

class NewsHandler(handler.Handler):
    """Class that handles news page. Shows new recipes published."""
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()

    def get(self):
        # Query last 10 published recipes.  ordered by creation date.
        limit = 10
        recipes = self.query_recipes.search_new_recipes(limit)

        # Render news page.
        self.render("news.html", recipes=recipes)
