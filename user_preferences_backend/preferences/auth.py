from .models import AccountSettings
from django.contrib.auth.hashers import check_password

def authenticate(email, password):
    try:
        user = AccountSettings.objects.get(email=email)
        if check_password(password, user.password):
            return user
    except AccountSettings.DoesNotExist:
        return None
    return None