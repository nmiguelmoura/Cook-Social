import time
import handler
import prefabs.cookie_handler
import prefabs.db_query_comments
import prefabs.db_query_users

class DeleteCommentHandler(handler.Handler):
    """Class that handles comment deletion."""

    cookies = prefabs.cookie_handler.CookieHandler()
    query_comments = prefabs.db_query_comments.DBQueryComments()
    query_users = prefabs.db_query_users.DBQueryUsers()

    def recipe_valid_access(self):
        # Get user id and comment id.
        user_id = self.get_user_id()
        comment_id = self.request.get("id")

        if comment_id:
            # If there is a comment id, search for it in db through id.
            comment = self.query_comments.search_comments_by_id(comment_id)

            if comment and comment.user_id == user_id:
                # If comment exists in db and the user editing is the same that
                # created the comment, return data.
                return {
                    "comment_id": comment_id,
                    "comment": comment,
                    "user": self.get_user(user_id)
                }
            else:
                # If comment doesn't exist in db or comment author is not the
                # one who is logged in, redirect to error message page.
                self.redirect("messagetouser?type=comment_permission_error")
        else:
            # If there is no comment id, redirect to error message.
            self.redirect("/messagetouser")

    def get_user_id(self):
        # Get user id stored in cookie.
        return self.cookies.get_loginfo_cookie(self)

    def get_user(self, user_id):
        # Get GqlQuery user object
        return self.query_users.search_user_by_id(user_id)

    def post(self):
        # Check if comment id matches comment in db and check if comment author
        # is the same that is logged in.
        validation = self.recipe_valid_access()

        if validation:
            # If data is valid, perform deletion

            comment = validation["comment"]

            # Get recipe_id to redirect user to recipe page after deletion.
            recipe_id = comment.recipe_id

            # Delete comment.
            comment.delete()

            # Delay 0.1 sec before redirecting to avoid error reading db on
            # recipe page.
            time.sleep(0.1)
            self.redirect("/recipe?id=%s" % recipe_id)
