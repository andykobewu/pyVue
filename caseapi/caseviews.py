from django.contrib.auth.models import User, Group
from rest_framework import viewsets,generics
from caseapi.serializers import UserSerializer, GroupSerializer
from caseapi.models import Case
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import permissions
from django.shortcuts import render

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



class CaswList(generics.ListCreateAPIView):
    """
    get:
    Return all case.
    post:
    Create a new case instance.
    """

    queryset = Case.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


