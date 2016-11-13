import prefabs.send_message
import prefabs.signup_validation
import handler


class ContactHandler(handler.Handler):
    """Class that handles contact form."""
    validation = prefabs.signup_validation.SignupValidation()
    send_message = prefabs.send_message.SendMessage()

    def get(self):
        self.render("contact.html")

    def post(self):
        # Get email and message from post command
        email = self.request.get("email")
        message = self.request.get("message")

        # Generate error message if comment box is empty.
        error_comment = "Empty message. Please send us your" \
                        " questions or suggestions." if message == "" else ""

        # Validate email.
        email_validation = self.validation.email_verify(email)

        if email_validation["response"] and message != "":
            # If email is valid and there is a message, send email.
            self.send_message.send_contact(email, message)

            # After email sent, redirect to page with message to user.
            self.redirect("/messagetouser?type=contact")
        else:
            # If email is not valid or there is no message,
            # render page with error messages.
            self.render("contact.html", email=email, message=message,
                        error_email=email_validation["info"],
                        error_comment=error_comment)

