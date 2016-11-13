import handler
import prefabs.cookie_handler
import prefabs.db_query_recipes
import prefabs.db_query_users

class KitchenHandler(handler.Handler):
    """Class that handles kitchen page with new publisheed recipes."""
    cookies = prefabs.cookie_handler.CookieHandler()
    query_recipes = prefabs.db_query_recipes.DBQueryRecipes()
    query_users = prefabs.db_query_users.DBQueryUsers()

    def get(self):
        # Get user id stored in cookies.
        user_id = self.cookies.get_loginfo_cookie(self)

        if user_id:
            # If user is logged, get user entity.
            user = self.query_users.search_user_by_id(user_id)

            if user:
                # If user exists, render the page.

                # Get username.
                username = user.username

                # Get new recipes from db ordered by creation date.
                limit = 10
                recipes = self.query_recipes.search_new_recipes(limit)

                # Render page.
                self.render("kitchen.html", user_id=user_id, username=username,
                            recipes=recipes)
            else:
                # If user doesn't exist in db, redirect to login page.
                self.redirect("/login")
        else:
            # # If user is not logged in, redirect to login page.
            self.redirect("/login")
