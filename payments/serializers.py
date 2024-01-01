from rest_framework import serializers
from .models import *


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
        depth = 1
