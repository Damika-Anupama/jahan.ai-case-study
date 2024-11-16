from django.db import models

class AccountSettings(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class NotificationSettings(models.Model):
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

    user = models.ForeignKey(AccountSettings, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES)
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)

class ThemeSettings(models.Model):
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

    user = models.ForeignKey(AccountSettings, on_delete=models.CASCADE)
    theme = models.CharField(max_length=50, choices=THEME_CHOICES)
    font_size = models.CharField(max_length=10, choices=FONT_SIZE_CHOICES)

class PrivacySettings(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROFILE_VISIBILITY_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    ]

    user = models.ForeignKey(AccountSettings, on_delete=models.CASCADE)
    profile_visibility = models.CharField(max_length=50, choices=PROFILE_VISIBILITY_CHOICES)
    data_sharing = models.BooleanField(default=True)