import handler

class MessageToUserHandler(handler.Handler):
    def get(self):
        type = self.request.get("type")
        print type
        message = None
        if type == "contact":
            message = " Your questions or sugestions have been sent. We will answer you as soon as possible. Thank you."
        elif type == "comment":
            message = "Your comment has been saved. Thanks for using Social Cook!"
        else:
            message = "The page you requested was not found!"

        self.render("message_to_user.html", message=message)
