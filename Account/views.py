from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins, generics
from Account.serializers import UserSerializer, GroupSerializer


class UserViewSet(generics.CreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
