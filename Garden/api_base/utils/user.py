import bcrypt
import base64


class UserUtils:

    @classmethod
    def hash_password(cls, raw_password):
        return base64.b64encode(raw_password)

    @classmethod
    def check_password(cls, raw_password, current_password):
        return bcrypt.checkpw(raw_password, current_password)
