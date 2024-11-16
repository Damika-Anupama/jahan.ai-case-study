from rest_framework import status
from django.db import transaction
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
from django.core.exceptions import ObjectDoesNotExist

class RegisterView(APIView):
    @transaction.atomic
    def post(self, request):
        data = request.data
        serializer = AccountSettingsSerializer(data=data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            try:
                NotificationSettings.objects.create(
                    user=user,
                    frequency='daily',
                    email_notifications=True,
                    push_notifications=True
                )
                ThemeSettings.objects.create(
                    user=user,
                    theme='light',
                    font_size='medium'
                )
                PrivacySettings.objects.create(
                    user=user,
                    profile_visibility='public',
                    data_sharing=True
                )
            except Exception as e:
                transaction.set_rollback(True)
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
            refresh = RefreshToken.for_user(user)
            return Response({
                'token': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdatePreferencesView(APIView):
    @transaction.atomic
    def patch(self, request, section):
        token = request.headers.get('Authorization').split(' ')[1]
        user = get_user_from_token(token)
        data = request.data
        
        try:
            if section == 'account_settings':
                instance = AccountSettings.objects.get(id=user.id)
                serializer = AccountSettingsSerializer(instance, data=data, partial=True)
            elif section == 'notification_settings':
                instance = NotificationSettings.objects.get(user_id=user.id)
                serializer = NotificationSettingsSerializer(instance, data=data, partial=True)
            elif section == 'theme_settings':
                instance = ThemeSettings.objects.get(user_id=user.id)
                serializer = ThemeSettingsSerializer(instance, data=data, partial=True)
            elif section == 'privacy_settings':
                instance = PrivacySettings.objects.get(user_id=user.id)
                serializer = PrivacySettingsSerializer(instance, data=data, partial=True)
            else:
                return Response({'detail': 'Invalid section'}, status=status.HTTP_400_BAD_REQUEST)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            transaction.set_rollback(True)
            return Response({"error": f"{section.replace('_', ' ').title()} not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            transaction.set_rollback(True)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

