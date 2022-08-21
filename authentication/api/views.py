from rest_framework import viewsets

from authentication.api.serializers import UserSerializer
from authentication.models import User


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
