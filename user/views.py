from django.contrib.auth.models import User
from google.oauth2 import id_token
from google.auth.transport import requests

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import GoogleLoginSerializer


class AuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    @action(detail=False, methods=["post"])
    def google_login(self, request):
        serializer = GoogleLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data["token"]

        try:
            user_info = id_token.verify_oauth2_token(
                token,
                requests.Request()
            )

            email = user_info["email"]
            name = user_info.get("name", "")

            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    "username": email,
                    "first_name": name,
                }
            )

            refresh = RefreshToken.for_user(user)

            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                },
                "is_new_user": created
            })

        except ValueError:
            return Response(
                {"error": "Invalid Google token"},
                status=status.HTTP_400_BAD_REQUEST
            )