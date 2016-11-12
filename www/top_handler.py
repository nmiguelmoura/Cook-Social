import handler
import prefabs.db_query_recipes

class TopHandler(handler.Handler):
    """Class that handles top voted page. Shows recipes with largest number of points."""

    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()

    def get(self):
        # Query last 10 published recipes.  ordered by points.
        limit = 10
        recipes = self.query_recipes.search_top_recipes(limit)

        # Render top page.
        self.render("top.html", recipes=recipes)