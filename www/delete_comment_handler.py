import time
import handler
import prefabs.cookie_handler
import prefabs.db_query_comments
import prefabs.db_query_users

class DeleteCommentHandler(handler.Handler):
    cookies = prefabs.cookie_handler.CookieHandler()
    query_comments = prefabs.db_query_comments.DBQueryComments()
    query_users = prefabs.db_query_users.DBQueryUsers()

    def recipe_valid_access(self):
        user_id = self.get_user_id()
        comment_id = self.request.get("id")

        if comment_id:
            comment = self.query_comments.search_comments_by_id(comment_id)

            if comment and comment.user_id == user_id:
                return {
                    "comment_id": comment_id,
                    "comment": comment,
                    "user": self.get_user(user_id)
                }
            else:
                self.redirect("messagetouser?type=comment_permission_error")
        else:
            self.redirect("/messagetouser")

    def get_user_id(self):
        return self.cookies.get_loginfo_cookie(self)

    def get_user(self, user_id):
        return self.query_users.search_user_by_id(user_id)

    def post(self):
        validation = self.recipe_valid_access()
        if validation:
            comment = validation["comment"]
            recipe_id = comment.recipe_id
            comment.delete()

            user = validation["user"]
            user.comments.remove(validation["comment_id"])
            user.put()
            time.sleep(0.1)
            self.redirect("/recipe?id=%s" % recipe_id)
