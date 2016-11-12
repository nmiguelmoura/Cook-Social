import time
import handler
import prefabs.cookie_handler
import prefabs.db_query_comments

class EditCommentHandler(handler.Handler):
    """Class that handles the edition of comments."""
    cookies = prefabs.cookie_handler.CookieHandler()
    query_comments = prefabs.db_query_comments.DBQueryComments()

    def get_comment_id(self):
        # Return comment id.
        return self.request.get("id")

    def get_comment(self, comment_id):
        # Return GqlQuery comment object through its id.
        return self.query_comments.search_comments_by_id(comment_id)

    def get_user_id(self):
        # Return user id stored in cookies.
        return self.cookies.get_loginfo_cookie(self)

    def render_get(self, comment):
        # Render the edit_comment page.
        self.render("edit_comment.html", comment=comment.comment, recipe_id=comment.recipe_id, id=self.get_comment_id())

    def render_post(self, comment):
        # Get edited comment posted by user.
        new_comment = self.request.get("comment")
        if new_comment != "":
            # If there is a comment, update comment entitie in db.
            comment.comment = new_comment
            comment.put()

            # Delay 0.1 sec the redirect, to avoid errors reading from db in next page.
            time.sleep(0.1)
            self.redirect("/recipe?id=%s" % comment.recipe_id)
        else:
            # If comment field is empty, render page with error message.
            self.render("edit_comment.html", id=self.get_comment_id(), recipe_id=comment.recipe_id, error_comment="The comment field is empty. Please insert a valid comment.")

    def validation(self, t):
        # Check if comment_id exists and comment author id matches user id logged in.

        # Get comment and user ids.
        comment_id = self.get_comment_id()
        user_id = self.get_user_id()

        if comment_id and user_id:
            # Get edited comment.
            comment = self.get_comment(comment_id)
            if comment and comment.user_id == user_id:
                # If comment exists and comment author id matches user id.
                if t == "get":
                    # Render page after get method.
                    self.render_get(comment)
                elif t == "post":
                    # Render page after post method.
                    self.render_post(comment)
            else:
                # If comment doesn't exists or comment author id is different than user id, show error message page.
                self.redirect("/messagetouser?type=comment_permission_error")
        else:
            # If comment id does not exist or user is not logged in, show error message page.
            self.redirect("/messagetouser?type=comment_permission_error")

    def get(self):
        # Check if data is valid.
        self.validation('get')

    def post(self):
        # Check if data is valid.
        self.validation('post')
