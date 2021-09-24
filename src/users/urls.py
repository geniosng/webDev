from django.urls import path

from .views import (
    user_login,
)

app_name = 'users'
urlpatterns = [
    path('login/', user_login, name='user_login'),
]