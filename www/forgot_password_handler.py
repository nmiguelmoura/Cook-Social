# -*- coding: utf-8 -*-

import random
import string

import handler
import prefabs.db_query_users
import prefabs.hash_tools
import prefabs.send_message
import prefabs.signup_validation


class ForgotPasswordHandler(handler.Handler):
    """Class that allows the recovery of user password. It sends an email with
    a randomly generated password that is stored in db. This class has to change
    to allow the input of username instead of email address. Username is unique,
    email address might not be."""

    validation = prefabs.signup_validation.SignupValidation()
    query_users = prefabs.db_query_users.DBQueryUsers()
    hashs = prefabs.hash_tools.HashTools()
    send_message = prefabs.send_message.SendMessage()

    def get(self):
        self.render("forgot_password.html")

    def post(self):
        # Get email posted by user.
        email = self.request.get("email")

        # Check if email is a valid one.
        email_validation = self.validation.email_verify(email)

        if email_validation["response"]:
            # If email is valid, check if its registered.
            user_email = self.check_email_registered(email)

            if user_email:
                # If email exists in db, generate new random password.
                new_password = self.generate_new_password(user_email.username)

                # Store new password in user entity associated to the email
                # address.
                user_email.password = new_password["hashed_password"]
                user_email.put()

                # Send email message to user with the new password.
                self.send_message.send_password(email,
                                                new_password["new_password"])

                # Redirect user to login page.
                self.redirect("login")
            else:
                # If email is not registered, render page with error message.
                self.render("forgot_password.html", email=email,
                            error_email=u"This email is not registered.")
        else:
            # If email is not valid, render page with error message.
            self.render("forgot_password.html", email=email,
                        error_email=email_validation["info"])

    def check_email_registered(self, email):
        # return user entity based on email address.
        return self.query_users.search_email(email)

    def generate_new_password(self, username):
        # Generate new random password.
        new_password = "".join(
            random.choice(string.ascii_letters) for _ in range(10))

        # Hash new password.
        hashed_password = self.hashs.make_secure_password(username,
                                                          new_password)

        # Return new password to send to user, and hashed password to store in db.
        return {
            "new_password": new_password,
            "hashed_password": hashed_password
        }
