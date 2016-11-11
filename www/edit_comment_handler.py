import time
import handler
import prefabs.cookie_handler
import prefabs.db_query_comments

class EditCommentHandler(handler.Handler):
    cookies = prefabs.cookie_handler.CookieHandler()
    query_comments = prefabs.db_query_comments.DBQueryComments()

    def get_comment_id(self):
        return self.request.get("id")

    def get_comment(self, comment_id):
        return self.query_comments.search_comments_by_id(comment_id)

    def get_user_id(self):
        return self.cookies.get_loginfo_cookie(self)

    def render_get(self, comment):
        self.render("edit_comment.html", comment=comment.comment, id=self.get_comment_id())

    def render_post(self, comment):
        new_comment = self.request.get("comment").encode("UTF-8")
        if new_comment != "":
            comment.comment = new_comment
            comment.put()
            time.sleep(0.1)
            self.redirect("/recipe?id=%s" % comment.recipe_id)
        else:
            self.render("edit_comment.html", id=self.get_comment_id(), error_comment="The comment field is empty. Please insert a valid comment.")

    def validation(self, t):
        comment_id = self.get_comment_id()
        user_id = self.get_user_id()
        if comment_id and user_id:
            comment = self.get_comment(comment_id)
            if comment and comment.user_id == user_id:
                if t == "get":
                    self.render_get(comment)
                elif t == "post":
                    self.render_post(comment)
            else:
                self.redirect("/messagetouser?type=comment_permission_error")
        else:
            self.redirect("/messagetouser?type=comment_permission_error")

    def get(self):
        self.validation('get')

    def post(self):
        self.validation('post')
