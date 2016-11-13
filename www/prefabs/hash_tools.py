import hashlib
import hmac
import random
import string

import secret


class HashTools():
    """Class that hashes passwords and performs cookie and
    password verification."""

    # Instantiate PreSecretCode class.
    SECRET = secret.SecretCode().get_secret_code()

    def __init__(self):
        pass

    def make_salt(self):
        # Return random string with 5 characters.
        return "".join(random.choice(string.ascii_letters) for _ in range(5))

    def make_secure_password(self, username, password, salt=None):
        # Make a secure hased password.
        if not salt:
            # If no salt has been passed, create new.
            salt = self.make_salt()

        # Return hashed password plus salt.
        return "%s|%s" % (
        hashlib.sha256(self.SECRET + username + password + salt).hexdigest(),
        salt)

    def check_secure_password(self, username, password, h):
        # Get salt from given password.
        salt = h.split("|")[1]

        # Get hashed password.
        return h == self.make_secure_password(username, password, salt)

    def hash_str(self, s):
        # Return hashed value.
        return hmac.new(self.SECRET, s).hexdigest()

    def make_secure_value(self, s):
        # Return value s and hashed s.
        return str("%s|%s" % (s, self.hash_str(s)))

    def check_cookie_val(self, h):
        # Split id from hashed value.
        val = h.split("|")[0]

        # Check if h value matches hashed id
        if h == self.make_secure_value(val):
            return val
