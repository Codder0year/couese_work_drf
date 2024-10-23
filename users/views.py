from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import CustomUser
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny, )

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()