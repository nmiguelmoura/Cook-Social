class PreSecretCode:
    """Class that stores secret codes and login info."""

    def __init__(self):
        pass

    def get_secret_code(self):
        # Secret code to hash
        return "2zJLwQaMtAT8D4Y3"

    def get_mailgun_login(self):
        # Return mailgun login data.
        return {
            "login":"postmaster@sandbox2bdfae1c853347ccad7c22abfc9eb3d7.mailgun.org",
            "password":"a32599821f6d86a63df229ae931905d1"
        }
