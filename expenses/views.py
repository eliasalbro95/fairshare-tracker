from django.shortcuts import render
from rest_framework.generics import ListAPIView
from expenses.models import Expenses
from expenses.serializers import ExpensesSerializer


# Create your views here.


class ExpensesListView(ListAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
