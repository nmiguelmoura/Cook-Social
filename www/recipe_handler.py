# -*- coding: utf-8 -*-

import handler
import prefabs.db_query_recipes
import prefabs.db_query_users
import prefabs.db_query_comments
import prefabs.cookie_handler


class RecipeHandler(handler.Handler):
    """Class that handles each individual recipe page."""

    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()
    query_users = prefabs.db_query_users.DBQueryUsers()
    query_comments = prefabs.db_query_comments.DBQueryComments()
    cookies = prefabs.cookie_handler.CookieHandler()

    def render_page(self, id, recipe, author, user_id, user_pointed, comments,
                    alert_window=False, alert_message=""):
        # Render page with all parameters
        self.render("recipe.html", id=id, title=recipe.title, author=author,
                    author_id=recipe.user_id,
                    image=recipe.image, prep_time=recipe.prep_time,
                    ingredients=recipe.ingredients, steps=recipe.steps,
                    user_id=user_id, points=recipe.points,
                    user_pointed=user_pointed, comments=comments,
                    alert_window=alert_window, alert_message=alert_message)

    def check_if_user_pointed(self, user, recipe_id):
        # Return if user has already attributed 1 point to this recipe
        for p in user.pointed:
            if p == recipe_id:
                return True

        return False

    def get_comments(self, recipe_id):
        # return comments on this recipe
        return self.query_comments.search_comments_by_recipe_id(recipe_id)

    def get_values(self):
        # Get recipe id.
        id = self.request.get("id")

        # Get recipe entity from db.
        recipe = self.query_recipes.search_recipes_by_id(id)

        # Get recipe author.
        author = recipe.user

        # Get user id stored in cookie.
        user_id = self.cookies.get_loginfo_cookie(self)

        # Get recipe comments.
        comments = self.get_comments(id)

        user = None
        user_pointed = None

        if user_id:
            # Run if user is logged.

            # Query user.
            user = self.query_users.search_user_by_id(user_id)

            # Check if user has already attributed 1 point to this recipe.
            user_pointed = self.check_if_user_pointed(user, id)

        # Return relevant data.
        return {
            "id": id,
            "recipe": recipe,
            "recipe_author": author,
            "user_id": user_id,
            "user": user,
            "user_pointed": user_pointed,
            "comments": comments
        }

    def manage_point(self, values):
        # Create var that points to user entity.
        user = values["user"]

        # Create var that points to recipe entity.
        recipe = values["recipe"]

        if values["user_pointed"]:
            # If user has already attributed 1 point, remove point from recipe.
            recipe.points -= 1

            # Remove recipe id from list points in user entity.
            user.pointed.remove(values["id"])

            values["user_pointed"] = False
        else:
            # If user hasn't attributed 1 point to this recipe, append recipe
            # id to list points in user.
            user.pointed.append(values["id"])

            # Add one point to recipe existing points.
            recipe.points += 1

            values["user_pointed"] = True

        # Store updated recipe entity.
        recipe.put()

        # Store updated user entity.
        user.put()

    def get(self):
        # Get recipe data.
        values = self.get_values()

        if values["recipe"]:
            # If recipe exists, render recipe page with corresponding data.
            self.render_page(values["id"], values["recipe"],
                             values["recipe_author"], values["user_id"],
                             values["user_pointed"], values["comments"])
        else:
            # If recipe does not exist, redirect to error message page.
            self.redirect("/messagetouser?type=notfound")

    def post(self):
        # This post function allows the current user to add or remove 1 point
        # to recipe.
        # Each user can only add or remove 1 point to each recipe.

        # Get recipe data.
        values = self.get_values()

        if values["user_id"]:
            # Run if user is logged in.
            if values["user_id"] == values["recipe"].user_id:
                # If logged user id matches recipe author id, render page with
                # alert window.
                # An author can't point his/her own recipe.
                self.render_page(values["id"], values["recipe"],
                                 values["recipe_author"], values["user_id"],
                                 values["user_pointed"], values["comments"],
                                 alert_window=True,
                                 alert_message="Não pode votar nas suas próprias "
                                               "receitas!")
            else:
                # If logged user is not recipe author, allow to add or
                # remove point.
                self.manage_point(values)

                # Render page with parameters.
                self.render_page(values["id"], values["recipe"],
                                 values["recipe_author"], values["user_id"],
                                 values["user_pointed"], values["comments"])
        else:
            # If user is logged out, redirect to login page.
            self.redirect("/login")
