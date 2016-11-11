import handler
import prefabs.db_query_recipes
import prefabs.db_query_users
import prefabs.cookie_handler

class RecipeHandler(handler.Handler):
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()
    query_users = prefabs.db_query_users.DBQueryUsers()
    cookies = prefabs.cookie_handler.CookieHandler()

    def render_page(self, id, recipe, author, user_id, user_pointed, alert_window=False, alert_message=""):
        self.render("recipe.html", id=id, title=recipe.title, author=author, author_id=recipe.user_id,
                    image=recipe.image, prep_time=recipe.prep_time, ingredients=recipe.ingredients, steps=recipe.steps, user_id=user_id, points=recipe.points, user_pointed=user_pointed, alert_window=alert_window, alert_message=alert_message)

    def check_if_user_pointed(self, user, recipe_id):
        for p in user.pointed:
            if p == recipe_id:
                return True

        return False

    def get_values(self):
        id = self.request.get("id")
        recipe = self.query_recipes.search_recipes_by_id(id)
        author = recipe.user
        user_id = self.cookies.get_loginfo_cookie(self)

        user = None
        user_pointed = None

        if user_id:
            user = self.query_users.search_user_by_id(user_id)
            user_pointed = self.check_if_user_pointed(user, id)

        return {
            "id": id,
            "recipe": recipe,
            "recipe_author": author,
            "user_id": user_id,
            "user": user,
            "user_pointed": user_pointed
        }

    def manage_point(self, values):
        user = values["user"]
        recipe = values["recipe"]
        if values["user_pointed"]:
            recipe.points -= 1
            user.pointed.remove(values["id"])
            values["user_pointed"] = False
        else:
            user.pointed.append(values["id"])
            recipe.points += 1
            values["user_pointed"] = True

        recipe.put()
        user.put()

    def get(self):
        values = self.get_values()

        if values["recipe"]:
            self.render_page(values["id"], values["recipe"], values["recipe_author"], values["user_id"], values["user_pointed"])
        else:
            self.redirect("/messagetouser?type=notfound")

    def post(self):
        values = self.get_values()

        if values["user_id"]:
            if values["user_id"] == values["recipe"].user_id:
                self.render_page(values["id"], values["recipe"], values["recipe_author"], values["user_id"], values["user_pointed"], alert_window=True, alert_message="You can't vote in your own recipes!")
            else:
                self.manage_point(values)
                self.render_page(values["id"], values["recipe"], values["recipe_author"], values["user_id"],
                                 values["user_pointed"])
        else:
            self.redirect("/login")