# -*- coding: utf-8 -*-

import time
import handler
import prefabs.cookie_handler
import prefabs.db_query_recipes
import prefabs.recipe_validation
from google.appengine.api import images


class EditRecipeHandler(handler.Handler):
    """Class that allows recipe author to edit a stored recipe."""

    cookies = prefabs.cookie_handler.CookieHandler()
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()
    recipe_validation = prefabs.recipe_validation.RecipeValidation()

    def recipe_valid_access(self):
        # Get user and recipe ids.
        user_id = self.get_user()
        recipe_id = self.request.get("id")

        if recipe_id:
            # If recipe id exists, get recipe entity from db.
            recipe = self.query_recipes.search_recipes_by_id(recipe_id)

            if recipe and recipe.user_id == user_id:
                # If recipe exists in db and recipe author is the same user
                # that is logged in, return recipe entity and id.
                return {"id": recipe_id, "recipe": recipe}
            else:
                # If recipe doesn't exists or recipe author doesn't match user
                # id, redirect to error message page.
                self.redirect("messagetouser?type=permission_error")
        else:
            # If recipe id doesn't exist, redirect to error message page.
            self.redirect("/messagetouser")

    def get_user(self):
        # return user id stored in cookies.
        return self.cookies.get_loginfo_cookie(self)

    def get(self):
        # Check if recipe exists and if user is the recipe author.
        validation_data = self.recipe_valid_access()

        if validation_data:
            # If data is valid, render page with stored recipe info.
            recipe = validation_data["recipe"]
            self.render("edit_recipe.html", id=validation_data["id"],
                        title=recipe.title, prep_time=recipe.prep_time,
                        category=recipe.category,
                        num_ingredients=len(recipe.ingredients),
                        ingredients=recipe.ingredients,
                        num_steps=len(recipe.steps),
                        steps=recipe.steps)

    def post(self):
        # Check if recipe exists and if user is the recipe author.
        validation_data = self.recipe_valid_access()

        if validation_data:
            # If recipe is valid, try to store new data.

            # Get recipe entity.
            recipe = validation_data["recipe"]

            # Get new title posted by user.
            title = self.request.get("title")

            # Get category.
            category = self.request.get("category")

            # Get new preparation time posted by user
            prep_time = self.request.get("prep_time")

            # Check the number of ingredients selected by user.
            num_ingredients = int(self.request.get("num_ing"))

            # Create a list to store ingredients.
            ingredients = []

            # Loop through each ingredient box available and previously
            # selected by user.
            for i in range(0, num_ingredients):
                # Get text edited by user.
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
                # Get text edited by user.
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
            category_validation = self.recipe_validation.validate_category(
                category)
            prep_time_validation = self.recipe_validation.validate_prep_time(
                prep_time)
            ingredients_validation = self.recipe_validation.list_length_validation(
                ingredients, u"ingrediente")
            steps_validation = self.recipe_validation.list_length_validation(
                steps, u"passo")

            if title_validation["response"] and \
                    category_validation["response"] and \
                    prep_time_validation["response"] and \
                    ingredients_validation["response"] and \
                    steps_validation["response"]:
                # If data posted is valid, udpdate recipe entity.
                recipe.title = title
                recipe.category = category
                recipe.prep_time = int(prep_time)
                recipe.ingredients = ingredients
                recipe.steps = steps
                if image:
                    # update image only if author has submited one.
                    recipe.image = image

                # Put recipe entity.
                recipe.put()

                # Get recipe key.
                recipe_key = recipe.key().id()

                # Delay 0.1 sec before redirect to recipe page to avoid errors
                # reading db.
                time.sleep(0.1)

                # Redirect to recipe page.
                self.redirect("/recipe?id=%s" % recipe_key)
            else:
                # If data posted is not valid, render page with error messages.
                self.render("edit_recipe.html", id=validation_data["id"],
                            title=title, prep_time=prep_time,
                            category=category,
                            ingredients=ingredients, steps=steps,
                            error_title=title_validation["info"],
                            error_category=category_validation["info"],
                            error_prep_time=prep_time_validation["info"],
                            error_ingredients=ingredients_validation["info"],
                            error_steps=steps_validation["info"],
                            num_ingredients=num_ingredients,
                            num_steps=num_steps)
