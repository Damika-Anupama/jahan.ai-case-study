from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    PreferencesView,
    UpdatePreferencesView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('preferences/', PreferencesView.as_view(), name='preferences'),
    path('preferences/<str:section>/', UpdatePreferencesView.as_view(), name='update-preferences'),
]