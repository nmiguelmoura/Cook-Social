# -*- coding: utf-8 -*-

import handler
import prefabs.db_query_recipes

class TopHandler(handler.Handler):
    """Class that handles top voted page. Shows recipes with largest
    number of points."""

    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()

    def get(self):
        # Get results page number.
        offset = self.request.get('page') if self.request.get('page') else '0'

        # Transform string into int.
        offset = int(offset)

        # Query last 10 published recipes.  ordered by points.
        limit = 1
        recipes = self.query_recipes.search_top_recipes(limit, offset)

        offset_previous = False
        offset_next = False

        # Check if button previous should be shown.
        if offset > 0:
            offset_previous = True

        # Check if button more recipes should be shown.
        # count recipe query results.
        count = recipes.count()

        if offset + limit < count:
            # If there are more recipes to show after this page, show the button.
            offset_next = True

        # Render top page.
        self.render("top.html", recipes=recipes, offset_previous=offset_previous,
                    offset_next=offset_next, offset_previous_page=offset-limit, offset_next_page=offset+limit)