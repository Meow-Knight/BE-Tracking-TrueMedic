from django.contrib.auth.hashers import check_password

from api_garden.models import User


class UserService:

    @classmethod
    def is_valid_login_data(cls, user_data):
        email = user_data.get("email", '')
        password = user_data.get("password", '')

        if not email or not password:
            return False

        user_queryset = User.objects.filter(email=email)
        if not user_queryset.exists():
            return False

        user = user_queryset.first()
        is_correct_password = check_password(password, user.password)
        if not is_correct_password:
            return False
        return True
