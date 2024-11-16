from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AccountSettings, NotificationSettings, ThemeSettings, PrivacySettings
from .serializers import (
    AccountSettingsSerializer,
    NotificationSettingsSerializer,
    ThemeSettingsSerializer,
    PrivacySettingsSerializer
)
from .auth import authenticate, get_user_from_token
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'token': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class PreferencesView(APIView):
    def get(self, request):
        token = request.headers.get('Authorization').split(' ')[1]
        user = get_user_from_token(token)
        print (user)
        try:
            account_settings = AccountSettings.objects.get(id=user.id)
            notification_settings = NotificationSettings.objects.get(user_id=user.id)
            theme_settings = ThemeSettings.objects.get(user_id=user.id)
            privacy_settings = PrivacySettings.objects.get(user_id=user.id)
            
            data = {
                'account_settings': AccountSettingsSerializer(account_settings).data,
                'notification_settings': NotificationSettingsSerializer(notification_settings).data,
                'theme_settings': ThemeSettingsSerializer(theme_settings).data,
                'privacy_settings': PrivacySettingsSerializer(privacy_settings).data,
            }
            return Response(data, status=status.HTTP_200_OK)
        except (AccountSettings.DoesNotExist, NotificationSettings.DoesNotExist, ThemeSettings.DoesNotExist, PrivacySettings.DoesNotExist):
            return Response({"error": "Preferences not found"}, status=status.HTTP_404_NOT_FOUND)

class UpdatePreferencesView(APIView):
    def put(self, request, section):
        user = request.user
        data = request.data
        
        if section == 'account':
            instance = AccountSettings.objects.get(user=user)
            serializer = AccountSettingsSerializer(instance, data=data, partial=True)
        elif section == 'notifications':
            instance = NotificationSettings.objects.get(user=user)
            serializer = NotificationSettingsSerializer(instance, data=data, partial=True)
        elif section == 'theme':
            instance = ThemeSettings.objects.get(user=user)
            serializer = ThemeSettingsSerializer(instance, data=data, partial=True)
        elif section == 'privacy':
            instance = PrivacySettings.objects.get(user=user)
            serializer = PrivacySettingsSerializer(instance, data=data, partial=True)
        else:
            return Response({'detail': 'Invalid section'}, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountSettingsView(APIView):
    def get(self, request):
        try:
            settings = AccountSettings.objects.get(user=request.user)
            serializer = AccountSettingsSerializer(settings)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AccountSettings.DoesNotExist:
            return Response({"error": "Account settings not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = AccountSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        try:
            settings = AccountSettings.objects.get(user=request.user)
            serializer = AccountSettingsSerializer(settings, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AccountSettings.DoesNotExist:
            return Response({"error": "Account settings not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        try:
            settings = AccountSettings.objects.get(user=request.user)
            settings.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AccountSettings.DoesNotExist:
            return Response({"error": "Account settings not found"}, status=status.HTTP_404_NOT_FOUND)

class NotificationSettingsView(APIView):
    def get(self, request):
        try:
            settings = NotificationSettings.objects.get(user=request.user)
            serializer = NotificationSettingsSerializer(settings)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotificationSettings.DoesNotExist:
            return Response({"error": "Notification settings not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = NotificationSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        try:
            settings = NotificationSettings.objects.get(user=request.user)
            serializer = NotificationSettingsSerializer(settings, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except NotificationSettings.DoesNotExist:
            return Response({"error": "Notification settings not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        try:
            settings = NotificationSettings.objects.get(user=request.user)
            settings.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotificationSettings.DoesNotExist:
            return Response({"error": "Notification settings not found"}, status=status.HTTP_404_NOT_FOUND)

class ThemeSettingsView(APIView):
    def get(self, request):
        try:
            settings = ThemeSettings.objects.get(user=request.user)
            serializer = ThemeSettingsSerializer(settings)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ThemeSettings.DoesNotExist:
            return Response({"error": "Theme settings not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ThemeSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        try:
            settings = ThemeSettings.objects.get(user=request.user)
            serializer = ThemeSettingsSerializer(settings, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ThemeSettings.DoesNotExist:
            return Response({"error": "Theme settings not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        try:
            settings = ThemeSettings.objects.get(user=request.user)
            settings.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ThemeSettings.DoesNotExist:
            return Response({"error": "Theme settings not found"}, status=status.HTTP_404_NOT_FOUND)

class PrivacySettingsView(APIView):
    def get(self, request):
        try:
            settings = PrivacySettings.objects.get(user=request.user)
            serializer = PrivacySettingsSerializer(settings)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PrivacySettings.DoesNotExist:
            return Response({"error": "Privacy settings not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = PrivacySettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        try:
            settings = PrivacySettings.objects.get(user=request.user)
            serializer = PrivacySettingsSerializer(settings, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PrivacySettings.DoesNotExist:
            return Response({"error": "Privacy settings not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        try:
            settings = PrivacySettings.objects.get(user=request.user)
            settings.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PrivacySettings.DoesNotExist:
            return Response({"error": "Privacy settings not found"}, status=status.HTTP_404_NOT_FOUND)