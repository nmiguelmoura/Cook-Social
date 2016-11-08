import handler
import time
import db_model_recipes
import prefabs.db_query_users
import prefabs.cookie_handler
import prefabs.recipe_validation
from google.appengine.api import images


class PublishHandler(handler.Handler):
    cookies = prefabs.cookie_handler.CookieHandler()
    recipe_validation = prefabs.recipe_validation.RecipeValidation()

    def get(self):
        log_info = self.cookies.get_loginfo_cookie(self)
        if log_info:
            self.render("publish.html", ingredients=[], steps=[])
        else:
            self.render("login.html")

    def post(self):
        log_info = self.cookies.get_loginfo_cookie(self)

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

        if title_validation["response"] and prep_time_validation["response"] and ingredients_validation["response"] and steps_validation["response"]:
            recipe = db_model_recipes.RecipesDBModel(user_id=log_info, image=image if image else None, title=title, prep_time=int(prep_time),
                                                     ingredients=ingredients, steps=steps, points=0)
            recipe.put()
            recipe_key = recipe.key().id()
            time.sleep(0.1)
            self.redirect("/recipe?id=%s" % recipe_key)
        else:
            self.render("publish.html", title=title, prep_time=prep_time, ingredients=ingredients, steps=steps, error_title=title_validation["info"], error_prep_time=prep_time_validation["info"], error_ingredients=ingredients_validation["info"], error_steps=steps_validation["info"], num_ingredients=num_ingredients, num_steps=num_steps)
