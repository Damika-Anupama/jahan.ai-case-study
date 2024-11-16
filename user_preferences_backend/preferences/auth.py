from .models import AccountSettings
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed

def authenticate(email, password):
    try:
        user = AccountSettings.objects.get(email=email)
        print (user.password, password)
        if user.password == password:
            return user
        # if check_password(password, user.password):
        #     return user
    except AccountSettings.DoesNotExist:
        return None
    return None

def get_user_from_token(token):
    try:
        access_token = AccessToken(token)
        user_id = access_token['user_id']
        user = AccountSettings.objects.get(id=user_id)
        return user
    except Exception as e:
        raise AuthenticationFailed('Invalid token')