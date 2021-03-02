from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer


class UserRegistrationViewSet(viewsets.ModelViewSet):
    """
    Users registeration.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    http_method_names = ['post']
