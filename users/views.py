from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from users.models import CustomUser
from users.serializers import CustomUserRegisterSerializer, CustomUserSerializer

from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.response import Response

# Create your views here.


class UsersListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserRegisterView(CreateAPIView):
    model = get_user_model()
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(
            status=status.HTTP_201_CREATED,
            data={"status": 201, "message": "User has been created."},
        )
