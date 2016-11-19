# -*- coding: utf-8 -*-

import handler
import prefabs.db_query_users
import prefabs.cookie_handler
import prefabs.hash_tools


class LoginHandler(handler.Handler):
    """Class that handles the login of an existing user."""

    hashs = prefabs.hash_tools.HashTools()
    cookies = prefabs.cookie_handler.CookieHandler()
    query_users = prefabs.db_query_users.DBQueryUsers()

    def get(self):
        if self.cookies.get_loginfo_cookie(self):
            # If user is already logged in, redirect to kitchen.
            self.redirect("/kitchen")
        else:
            # If no user is logged in, render login page.
            self.render("login.html")

    def post(self):
        # Get username and password posted by user.
        username = self.request.get("username")
        password = self.request.get("password")

        # Check if user exists in db.
        existing_user = self.query_users.search_user(username)

        if existing_user:
            # If user exists in db, verify password.
            if self.verify_password(existing_user, password):
                # If password is correct, store cookie in system and redirect
                # to kitchen page.
                self.cookies.set_loginfo_cookie(self,
                                                str(existing_user.key().id()))
                self.redirect("/kitchen")
                return

        # Id user does not exist or password doesn't match, render page with
        # error message.
        self.render('login.html', username=username,
                    error_message="Nome de utilizador ou palavra-chave inválida.")

    def verify_password(self, existing_user, given_password):
        # Compare password posted and stored and return result.
        return self.hashs.check_secure_password(existing_user.username,
                                                given_password,
                                                existing_user.password)
