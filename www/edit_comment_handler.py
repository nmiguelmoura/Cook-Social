import handler

class EditCommentHandler(handler.Handler):
    def get(self):
        self.render("edit_comment.html")
