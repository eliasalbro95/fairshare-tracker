from django.shortcuts import render
from rest_framework.generics import ListAPIView

from payments.models import Payments
from payments.serializers import PaymentsSerializer

# Create your views here.


class PaymentsListView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
