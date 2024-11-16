from django.urls import path
from .views import (
    AccountSettingsView,
    NotificationSettingsView,
    ThemeSettingsView,
    PrivacySettingsView,
    LoginView,
    PreferencesView,
    UpdatePreferencesView
)

urlpatterns = [
    path('account/', AccountSettingsView.as_view(), name='account-settings'),
    path('notifications/', NotificationSettingsView.as_view(), name='notification-settings'),
    path('theme/', ThemeSettingsView.as_view(), name='theme-settings'),
    path('privacy/', PrivacySettingsView.as_view(), name='privacy-settings'),
    path('login/', LoginView.as_view(), name='login'),
    path('preferences/', PreferencesView.as_view(), name='preferences'),
    path('preferences/<str:section>/', UpdatePreferencesView.as_view(), name='update-preferences'),
]