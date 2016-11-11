import time
import handler
import prefabs.db_query_recipes
import prefabs.db_query_users
import prefabs.cookie_handler
import db_model_comments

class NewCommentHandler(handler.Handler):
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()
    query_users = prefabs.db_query_users.DBQueryUsers()
    cookies = prefabs.cookie_handler.CookieHandler()

    def get_user_id(self):
        return self.cookies.get_loginfo_cookie(self)

    def get_user(self, user_id):
        user = self.query_users.search_user_by_id(user_id)
        if user:
            return user

        return None

    def get_recipe(self):
        recipe_id = self.request.get("id")
        if recipe_id:
            return self.query_recipes.search_recipes_by_id(recipe_id)

        return None

    def render_get(self, recipe):
        self.render("new_comment.html", title=recipe.title)

    def render_post(self, recipe, user_id):
        comment = self.request.get("comment").encode('utf-8')
        if comment:
            user = self.get_user(user_id)
            recipe_id = self.request.get("id")
            comments = db_model_comments.CommentsDBModel(user_id=user_id, username=user.username, recipe_id=recipe_id, comment=comment)
            comments.put()
            comment_key = comments.key().id()

            user.comments.append(str(comment_key))
            user.put()
            time.sleep(0.1)
            self.redirect("/recipe?id=%s" % recipe_id)
        else:
            self.render("new_comment.html", error_comment="The comment field is empty. Please insert a valid comment.")

    def data_verification(self, t):
        user_id = self.get_user_id()
        if user_id:
            recipe = self.get_recipe()
            if recipe:
                if t == "get":
                    self.render_get(recipe)
                elif t == "post":
                    self.render_post(recipe, user_id)
            else:
                self.redirect("/messagetouser?type=recipe_not_found")
        else:
            self.redirect("/login")

    def get(self):
        self.data_verification("get")


    def post(self):
        self.data_verification("post")



