import time
import handler
import prefabs.cookie_handler
import prefabs.db_query_recipes
import prefabs.recipe_validation

class EditRecipeHandler(handler.Handler):
    cookies = prefabs.cookie_handler.CookieHandler()
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()
    recipe_validation = prefabs.recipe_validation.RecipeValidation()

    def recipe_valid_access(self):
        user_id = self.get_user()
        recipe_id = self.request.get("id")
        if recipe_id:
            recipe = self.query_recipes.search_recipes_by_id(recipe_id)

            if recipe and recipe.user_id == user_id:
                return {"id": recipe_id, "recipe": recipe}
            else:
                self.redirect("messagetouser?type=permission_error")
        else:
            self.redirect("/messagetouser")

    def get_user(self):
        return self.cookies.get_loginfo_cookie(self)

    def get(self):
        validation_data = self.recipe_valid_access()

        if validation_data:
            recipe = validation_data["recipe"]
            self.render("edit_recipe.html", id=validation_data["id"], title=recipe.title, prep_time=recipe.prep_time, num_ingredients=len(recipe.ingredients), ingredients=recipe.ingredients, num_steps=len(recipe.steps), steps=recipe.steps)

    def post(self):
        validation_data = self.recipe_valid_access()

        if validation_data:
            recipe = validation_data["recipe"]
            title = self.request.get("title")
            prep_time = self.request.get("prep_time")
            num_ingredients = int(self.request.get("num_ing"))
            ingredients = []
            for i in range(0, num_ingredients):
                ing = self.request.get("ing_%s" % i)
                if ing != "":
                    ingredients.append(ing)

            num_steps = int(self.request.get("num_steps"))
            steps = []
            for i in range(0, num_steps):
                step = self.request.get("step_%s" % i)
                if step != "":
                    steps.append(step)

            image = self.request.get("photo")

            title_validation = self.recipe_validation.validate_title(title)
            prep_time_validation = self.recipe_validation.validate_prep_time(prep_time)
            ingredients_validation = self.recipe_validation.list_length_validation(ingredients, "ingredient")
            steps_validation = self.recipe_validation.list_length_validation(steps, "step")

            if title_validation["response"] and prep_time_validation["response"] and ingredients_validation[
                "response"] and steps_validation["response"]:
                recipe.title = title
                recipe.prep_time = int(prep_time)
                recipe.ingredients = ingredients
                recipe.steps = steps
                if image:
                    recipe.image = image

                recipe.put()
                recipe_key = recipe.key().id()
                time.sleep(0.1)
                self.redirect("/recipe?id=%s" % recipe_key)
            else:
                self.render("publish.html", id=validation_data["id"], title=title, prep_time=prep_time, ingredients=ingredients, steps=steps, error_title=title_validation["info"], error_prep_time=prep_time_validation["info"], error_ingredients=ingredients_validation["info"], error_steps=steps_validation["info"], num_ingredients=num_ingredients, num_steps=num_steps)
