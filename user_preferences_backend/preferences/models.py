from django.db import models

class AccountSettings(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class NotificationSettings(models.Model):
    user = models.ForeignKey(AccountSettings, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=50)
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)

class ThemeSettings(models.Model):
    user = models.ForeignKey(AccountSettings, on_delete=models.CASCADE)
    theme = models.CharField(max_length=50)
    font_size = models.CharField(max_length=10)

class PrivacySettings(models.Model):
    user = models.ForeignKey(AccountSettings, on_delete=models.CASCADE)
    profile_visibility = models.CharField(max_length=50)
    data_sharing = models.BooleanField(default=True)
    