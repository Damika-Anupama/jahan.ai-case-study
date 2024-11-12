from rest_framework import serializers
from .models import AccountSettings, NotificationSettings, ThemeSettings, PrivacySettings
from django.core.validators import validate_email

class AccountSettingsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(validators=[validate_email])
    
    class Meta:
        model = AccountSettings
        fields = '__all__'
    
    def validate_username(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Username must contain only alphanumeric characters.")
        return value

class NotificationSettingsSerializer(serializers.ModelSerializer):
    frequency = serializers.ChoiceField(choices=["daily", "weekly"])

    class Meta:
        model = NotificationSettings
        fields = '__all__'
    
    def validate_frequency(self, value):
        if value not in ["daily", "weekly"]:
            raise serializers.ValidationError("Frequency must be either 'daily' or 'weekly'.")
        return value

class ThemeSettingsSerializer(serializers.ModelSerializer):
    color = serializers.CharField(max_length=50)
    font = serializers.CharField(max_length=50)
    layout = serializers.CharField(max_length=50)

    class Meta:
        model = ThemeSettings
        fields = '__all__'
    
    def validate_color(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Color must contain only alphanumeric characters.")
        return value

    def validate_font(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Font must contain only alphanumeric characters.")
        return value

    def validate_layout(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Layout must contain only alphanumeric characters.")
        return value
    
class PrivacySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacySettings
        fields = '__all__'
