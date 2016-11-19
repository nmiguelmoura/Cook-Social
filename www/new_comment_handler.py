# -*- coding: utf-8 -*-

import time
import handler
import prefabs.db_query_recipes
import prefabs.db_query_users
import prefabs.cookie_handler
import db_model_comments

class NewCommentHandler(handler.Handler):
    """Class that allows a registered and logged user to post a comment
    in a recipe."""

    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()
    query_users = prefabs.db_query_users.DBQueryUsers()
    cookies = prefabs.cookie_handler.CookieHandler()

    def get_user_id(self):
        # Return user id stored in cookie.
        return self.cookies.get_loginfo_cookie(self)

    def get_user(self, user_id):
        # Return user entity from db.
        user = self.query_users.search_user_by_id(user_id)
        if user:
            return user

        # Return None if user doesn't exist.
        return None

    def get_recipe(self):
        # Get recipe id from get method.
        recipe_id = self.request.get("id")

        if recipe_id:
            # If recipe id has been passed, search for recipe in db and
            # return recipe entity.
            return self.query_recipes.search_recipes_by_id(recipe_id)

        # return None if no recipe_id has been found.
        return None

    def render_get(self, recipe):
        # Render comment page with recipe title.
        self.render("new_comment.html", title=recipe.title)

    def render_post(self, recipe, user_id):
        # Get user comment.
        comment = self.request.get("comment")

        if comment:
            # Run if user posted a comment.

            # Get user id from cookie.
            user = self.get_user(user_id)

            # Get recipe id from get method.
            recipe_id = self.request.get("id")

            # Create new entity to store comment.
            comments = db_model_comments.CommentsDBModel(user_id=user_id,
                                                         username=user.username,
                                                         recipe_id=recipe_id,
                                                         comment=comment)
            comments.put()

            # Delay 0.1sec before redirecting to avoid errors reading db.
            time.sleep(0.1)

            # Redirect to recipe page with commented recipe_id.
            self.redirect("/recipe?id=%s" % recipe_id)
        else:
            # If comment field is empty, render page with error message.
            self.render("new_comment.html",
                        error_comment="O campo destinado ao comentário está vazio."
                                      " Por favor insira um comentário válido..")

    def data_verification(self, t):
        # Verify if user is logged in and recipe exists.

        # Get user id from cookie.
        user_id = self.get_user_id()

        if user_id:
            # If user is logged in, query recipe.
            recipe = self.get_recipe()

            if recipe:
                # Run if recipe exists.
                if t == "get":
                    # Run this function if method is get.
                    self.render_get(recipe)
                elif t == "post":
                    # Run this function if method is post.
                    self.render_post(recipe, user_id)
            else:
                # If recipe does not exist, show error_message_page.
                self.redirect("/messagetouser?type=recipe_not_found")
        else:
            # If user is not logged in, redirect to login page.
            self.redirect("/login")

    def get(self):
        # Verify user and recipe data.
        self.data_verification("get")


    def post(self):
        # Verify user and recipe data.
        self.data_verification("post")



