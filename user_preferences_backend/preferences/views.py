from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AccountSettings, NotificationSettings, ThemeSettings, PrivacySettings
from .serializers import AccountSettingsSerializer, NotificationSettingsSerializer, ThemeSettingsSerializer, PrivacySettingsSerializer

class AccountSettingsView(APIView):
    def get(self, request):
        settings = AccountSettings.objects.get(user=request.user)
        serializer = AccountSettingsSerializer(settings)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        settings = AccountSettings.objects.get(user=request.user)
        serializer = AccountSettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        settings = AccountSettings.objects.get(user=request.user)
        settings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request):
        settings = AccountSettings.objects.get(user=request.user)
        serializer = AccountSettingsSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class NotificationSettingsView(APIView):
    def get(self, request):
        settings = NotificationSettings.objects.get(user=request.user)
        serializer = NotificationSettingsSerializer(settings)
        return Response(serializer.data)

    def post(self, request):
        serializer = NotificationSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        settings = NotificationSettings.objects.get(user=request.user)
        serializer = NotificationSettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        settings = NotificationSettings.objects.get(user=request.user)
        settings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request):
        settings = NotificationSettings.objects.get(user=request.user)
        serializer = NotificationSettingsSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ThemeSettingsView(APIView):
    def get(self, request):
        settings = ThemeSettings.objects.get(user=request.user)
        serializer = ThemeSettingsSerializer(settings)
        return Response(serializer.data)

    def post(self, request):
        serializer = ThemeSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        settings = ThemeSettings.objects.get(user=request.user)
        serializer = ThemeSettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        settings = ThemeSettings.objects.get(user=request.user)
        settings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request):
        settings = ThemeSettings.objects.get(user=request.user)
        serializer = ThemeSettingsSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PrivacySettingsView(APIView):
    def get(self, request):
        settings = PrivacySettings.objects.get(user=request.user)
        serializer = PrivacySettingsSerializer(settings)
        return Response(serializer.data)

    def post(self, request):
        serializer = PrivacySettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        settings = PrivacySettings.objects.get(user=request.user)
        serializer = PrivacySettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        settings = PrivacySettings.objects.get(user=request.user)
        settings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request):
        settings = PrivacySettings.objects.get(user=request.user)
        serializer = PrivacySettingsSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    