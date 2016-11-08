import hashlib
import hmac
import random
import string

import secret_code


class HashTools():
    SECRET = secret_code.PreSecretCode().get_secret_code()

    def __init__(self):
        pass

    def make_salt(self):
        return "".join(random.choice(string.ascii_letters) for _ in range(5))

    def make_secure_password(self, username, password, salt=None):
        if not salt:
            salt = self.make_salt()

        return "%s|%s" % (hashlib.sha256(self.SECRET+username+password+salt).hexdigest(), salt)

    def check_secure_password(self, username, password, h):
        salt = h.split("|")[1]
        return h == self.make_secure_password(username, password, salt)

    def hash_str(self, s):
        return hmac.new(self.SECRET, s).hexdigest()

    def make_secure_value(self, s):
        return str("%s|%s" % (s, self.hash_str(s)))

    def check_cookie_val(self, h):
        val = h.split("|")[0]
        if h == self.make_secure_value(val):
            return val
