import random
import string

import handler
import prefabs.db_query_users
import prefabs.hash_tools
import prefabs.send_message
import prefabs.signup_validation


class ForgotPasswordHandler(handler.Handler):
    validation = prefabs.signup_validation.SignupValidation()
    query_users = prefabs.db_query_users.DBQueryUsers()
    hashs = prefabs.hash_tools.HashTools()
    send_message = prefabs.send_message.SendMessage()

    def get(self):
        self.render("forgot_password.html")

    def post(self):
        email = self.request.get("email")

        email_validation = self.validation.email_verify(email)

        if email_validation["response"]:
            user_email = self.check_email_registered(email)
            if user_email:
                new_password = self.generate_new_password(user_email.username)
                user_email.password = new_password["hashed_password"]
                user_email.put()

                self.send_message.send_password(email, new_password["new_password"])

                self.redirect("login")
            else:
                self.render("forgot_password.html", email=email, error_email="This email is not registered.")
        else:
            self.render("forgot_password.html", email=email, error_email=email_validation["info"])

    def check_email_registered(self, email):
        return self.query_users.search_email(email)

    def generate_new_password(self, username):
        new_password = "".join(random.choice(string.ascii_letters) for _ in range(10))
        hashed_password = self.hashs.make_secure_password(username, new_password)
        return {
            "new_password": new_password,
            "hashed_password": hashed_password
        }
