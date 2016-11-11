import prefabs.send_message
import prefabs.signup_validation
import handler


class ContactHandler(handler.Handler):
    validation = prefabs.signup_validation.SignupValidation()
    send_message = prefabs.send_message.SendMessage()

    def get(self):
        self.render("contact.html")

    def post(self):
        email = self.request.get("email")
        message = self.request.get("message").encode("UTF-8")
        error_comment = "Empty message. Please send us your questions or sugestions." if message == "" else ""
        email_validation = self.validation.email_verify(email)

        if email_validation["response"] and message != "":
            self.send_message.send_contact(email, message)
            self.redirect("/messagetouser?type=contact")
        else:
            self.render("contact.html", email=email, message=message, error_email=email_validation["info"], error_comment=error_comment)

