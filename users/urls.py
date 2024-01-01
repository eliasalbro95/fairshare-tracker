from django.contrib import admin
from django.urls import path, include

from users.views import UsersListView, CustomUserRegisterView

app_name = "users"


urlpatterns = [
    path("", UsersListView.as_view(), name="users-list"),
    path("register/", CustomUserRegisterView.as_view(), name="user-register"),
]
