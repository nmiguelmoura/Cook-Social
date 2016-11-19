# -*- coding: utf-8 -*-

import handler
import prefabs.cookie_handler
import prefabs.db_query_recipes

class MainHandler(handler.Handler):
    """Class that manages index page. This page is only viewed when user
    is not logged in, else is sent to kitchen."""
    cookies = prefabs.cookie_handler.CookieHandler()
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()

    def get(self):
        # Get user id stored in cookie.
        user_id = self.cookies.get_loginfo_cookie(self)

        if user_id:
            # If user is logged in, redirect to kitchen.
            self.redirect("/kitchen")
        else:
            # If user is not logged, render main page and show new recipes
            # published ordered by creation time.
            limit = 10
            recipes = self.query_recipes.search_new_recipes(limit)
            self.render("main.html", recipes=recipes)
