from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from .serializers import UserSerializer, GroupSerializer


class UserViewSEt(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSEt(UserSerializer):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Create your views here.
