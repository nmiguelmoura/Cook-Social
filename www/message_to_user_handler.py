import handler

class MessageToUserHandler(handler.Handler):
    """Class that handles error message page."""
    def get(self):
        # Get type of message to display
        type = self.request.get("type")

        # Create variables to store title and message and
        # change them according to type passed in.
        title = None
        message = None
        if type == "contact":
            title = "Question / suggestion sent"
            message = " Your questions or suggestions have been sent. " \
                      "We will answer you as soon as possible. Thank you."
        elif type == "comment_permission_error":
            title = "Permission error"
            message = "You are not allowed to edit this comment. " \
                      "You can only edit your own comments."
        elif type == "recipe_not_found":
            title = "Recipe not found"
            message = "The recipe you specified hasn't been found!"
        elif type == "permission_error":
            title = "Permission error"
            message = "You are not allowed to edit this recipe. " \
                      "You can only edit your own recipes."
        elif type == "unexpected_error":
            title = "Unexpected error"
            message = "An unexpected error has occured. " \
                      "Please try again."
        else:
            title = "Page not found"
            message = "The page you requested was not found!"

        # Render page with corresponding title and message.
        self.render("message_to_user.html", title=title, message=message)
