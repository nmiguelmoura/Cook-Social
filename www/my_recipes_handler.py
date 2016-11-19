# -*- coding: utf-8 -*-

import handler
import prefabs.db_query_recipes
import prefabs.db_query_users
import prefabs.cookie_handler


class MyRecipesHandler(handler.Handler):
    """Class that handles the recipes page. This page is like a blog that shows
    everything a user has posted."""

    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()
    query_users = prefabs.db_query_users.DBQueryUsers()
    cookies = prefabs.cookie_handler.CookieHandler()

    def render_content(self, user_id):
        # Get user entity through user_id.
        user = self.query_users.search_user_by_id(user_id)

        if user:
            # If user exists, get username to display on page title.
            username = user.username

            # Query recipes posted by the user_id.
            recipes = self.query_recipes.search_recipes_by_user_id(user_id)

            # If user has no recipes, store error_message.
            no_recipes_message = "" if recipes.count() > 0 else u"Este cozinheiro ainda não publicou nenhuma receita"

            # Render recipes page.
            self.render("my_recipes.html", username=username, recipes=recipes,
                        no_recipes_message=no_recipes_message)
        else:
            # If user does not exists, redirect to error message page.
            self.redirect("messagetouser")

    def get(self):
        # Create variable to store user id.
        user_id = None

        # Get user id from get method.
        get_id = self.request.get("id")

        if get_id:
            # If get method defines a user, store user id in user_id var, to
            # allow showing this users page.
            user_id = get_id
        else:
            # If get method does not defines a user, get user_id form currently
            # logged user.
            user_id = self.cookies.get_loginfo_cookie(self)

            if not user_id:
                # If user is not logged in (and obviously no user id was sent
                # through get method), redirect to loginpage.
                self.redirect("login")
                return

        # Render page related to user_id (passed through get method or got from
        # cookie)
        self.render_content(user_id)
