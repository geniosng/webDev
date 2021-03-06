from django.urls import path

from .views import (
    user_login,
    user_logout,
    user_signup,
    user_profile
)

app_name = 'users'
urlpatterns = [
    # localhost:8000/users/login/
    path('login/', user_login, name='user_login'),
    # localhost:8000/users/logout/
    path('logout/', user_logout, name='user_logout'),
    # localhost:8000/users/signup/
    path('signup/', user_signup, name='user_signup'),
    # localhost:8000/users/me/profile/
    path('me/profile/', user_profile, name='user_profile'),
]