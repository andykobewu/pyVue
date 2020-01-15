from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from caseapi.serializer import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API 允许查看或编辑用户
    """
    queryset = User.objects.all().order_by('create_time')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API 允许查看或编辑组
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
