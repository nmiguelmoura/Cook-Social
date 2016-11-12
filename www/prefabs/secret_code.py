class PreSecretCode:
    """Class that stores secret codes and login info."""

    def __init__(self):
        pass

    def get_secret_code(self):
        # Secret code to hash
        return "ABCDEFGH"

    def get_mailgun_login(self):
        # Return mailgun login data.
        return {
            "login":"postmaster@your_id.mailgun.org",
            "password":"1234"
        }
