# -*- coding: utf-8 -*-

import handler
import time
import db_model_recipes
import prefabs.db_query_users
import prefabs.cookie_handler
import prefabs.recipe_validation
import prefabs.db_query_users
from google.appengine.api import images


class PublishHandler(handler.Handler):
    """Class that handles the publication of new recipes."""

    cookies = prefabs.cookie_handler.CookieHandler()
    recipe_validation = prefabs.recipe_validation.RecipeValidation()
    query_users = prefabs.db_query_users.DBQueryUsers()

    def get(self):
        # Get user id stored in cookie.
        log_info = self.cookies.get_loginfo_cookie(self)

        if log_info:
            # If user is logged in, render publish page.
            self.render("publish.html", ingredients=[], steps=[])
        else:
            # If user is not logegd in, redirect to login page.
            self.redirect("/login")

    def post(self):
        # Get user id stored in cookie.
        log_info = self.cookies.get_loginfo_cookie(self)

        if log_info:
            # If user is logged in, get posted data, validate and store.

            # Get username from logged user..
            user = self.query_users.search_user_by_id(log_info).username

            # Get posted recipe title.
            title = self.request.get("title")

            # Get posted recipe preparation time.
            prep_time = self.request.get("prep_time")

            # Check the number of ingredients selected by user.
            num_ingredients = int(self.request.get("num_ing"))

            # Create a list to store ingredients.
            ingredients = []

            # Loop through each ingredient box available and previously
            # selected by user.
            for i in range(0, num_ingredients):
                # Get text posted by user.
                ing = self.request.get("ing_%s" % i)
                if ing != "":
                    # If field is not empty, store ingredient in
                    # ingredients list.
                    ingredients.append(ing)

            # Check the number of steps selected by user.
            num_steps = int(self.request.get("num_steps"))

            # Create a list to store steps.
            steps = []

            # Loop through each step box available and previously
            # selected by user.
            for i in range(0, num_steps):
                # Get text posted by user.
                step = self.request.get("step_%s" % i)
                if step != "":
                    # If field is not empty, store ingredient in steps list.
                    steps.append(step)

            # Get image selected by  user from input file.
            image = self.request.get("photo")

            if image:
                # Resize image. Only works if you have PIL installed.
                image = images.resize(image, 800)

            # Check if data posted is valid.
            title_validation = self.recipe_validation.validate_title(title)
            prep_time_validation = self.recipe_validation.validate_prep_time(
                prep_time)
            ingredients_validation = self.recipe_validation.list_length_validation(
                ingredients, u"ingrediente")
            steps_validation = self.recipe_validation.list_length_validation(
                steps, u"passo")

            if title_validation["response"] and prep_time_validation[
                "response"] and ingredients_validation["response"] and \
                    steps_validation["response"]:
                # If data posted is valid, store recipe entity.

                # Create new recipe.
                recipe = db_model_recipes.RecipesDBModel(user_id=log_info,
                                                         user=user,
                                                         image=image if image else None,
                                                         title=title,
                                                         prep_time=int(
                                                             prep_time),
                                                         ingredients=ingredients,
                                                         steps=steps, points=0)
                recipe.put()

                # Get recipe key.
                recipe_key = recipe.key().id()

                # Delay 0.1sec before redirect to next page, to avoid errors
                # reading db.
                time.sleep(0.1)

                # Redirect to newly created recipe page.
                self.redirect("/recipe?id=%s" % recipe_key)
            else:
                # If data posted is invalid, render page with corresponding
                # error messages.
                self.render("publish.html", title=title, prep_time=prep_time,
                            ingredients=ingredients, steps=steps,
                            error_title=title_validation["info"],
                            error_prep_time=prep_time_validation["info"],
                            error_ingredients=ingredients_validation["info"],
                            error_steps=steps_validation["info"],
                            num_ingredients=num_ingredients,
                            num_steps=num_steps)
        else:
            # If user is not logged in, redirect to error message page.
            self.redirect("/messagetouser")
