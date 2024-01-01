from django.contrib import admin
from django.urls import path, include
from .views import ExpensesListView

app_name = "expenses"


urlpatterns = [
    path("", ExpensesListView.as_view(), name="expenses-list"),
]
