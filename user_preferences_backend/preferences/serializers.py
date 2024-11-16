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
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    ON_DEMAND = 'on-demand'
    FREQUENCY_CHOICES = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
        (ON_DEMAND, 'On-demand'),
    ]

    frequency = serializers.ChoiceField(choices=[choice[0] for choice in FREQUENCY_CHOICES])

    class Meta:
        model = NotificationSettings
        fields = '__all__'

class ThemeSettingsSerializer(serializers.ModelSerializer):
    LIGHT = 'light'
    DARK = 'dark'
    THEME_CHOICES = [
        (LIGHT, 'Light'),
        (DARK, 'Dark'),
    ]

    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    FONT_SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]

    theme = serializers.ChoiceField(choices=[choice[0] for choice in THEME_CHOICES])
    font_size = serializers.ChoiceField(choices=[choice[0] for choice in FONT_SIZE_CHOICES])

    class Meta:
        model = ThemeSettings
        fields = '__all__'

class PrivacySettingsSerializer(serializers.ModelSerializer):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROFILE_VISIBILITY_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    ]

    profile_visibility = serializers.ChoiceField(choices=[choice[0] for choice in PROFILE_VISIBILITY_CHOICES])

    class Meta:
        model = PrivacySettings
        fields = '__all__'