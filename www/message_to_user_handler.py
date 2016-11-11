import handler

class MessageToUserHandler(handler.Handler):
    def get(self):
        type = self.request.get("type")
        print type
        message = None
        if type == "contact":
            title = "Question / sugestion sent"
            message = " Your questions or sugestions have been sent. We will answer you as soon as possible. Thank you."
        elif type == "comment":
            title = "Comment saved"
            message = "Your comment has been saved. Thanks for using Social Cook!"
        elif type == "comment_permission_error":
            title = "Permission error"
            message = "You are not allowed to edit this comment. You can only edit your own comments."
        elif type == "recipe_not_found":
            title = "Recipe not found"
            message = "The recipe you specified hasn't been found!"
        elif type == "permission_error":
            title = "Permission error"
            message = "You are not allowed to edit this recipe. You can only edit your own recipes."
        else:
            title = "Page not found"
            message = "The page you requested was not found!"

        self.render("message_to_user.html", message=message)
