from django.contrib import admin
from django.urls import path, include

from payments.views import PaymentsListView

app_name = "payments"


urlpatterns = [
    path("", PaymentsListView.as_view(), name="payments-list"),
]
