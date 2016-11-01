import handler

class NewCommentHandler(handler.Handler):
    def get(self):
        self.render("new_comment.html")
