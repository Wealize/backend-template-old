from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


class BaseViewSet(ModelViewSet):
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated,)


class BaseTestCase(TestCase):
    BASE_URL = '/api/v1'

    def setUp(self):
        User = get_user_model()
        self.user1 = User.objects.create_user(
            username='testuser1', password='12345')
        self.user1.save()
        self.user2 = User.objects.create_user(
            username='testuser2', password='12345')
        self.user2.save()
        self.user1_token = self.create_jwt_for_user(self.user1)
        self.user2_token = self.create_jwt_for_user(self.user2)

    def create_jwt_for_user(self, user):
        return str(RefreshToken.for_user(user).access_token)

    def create_user(self, username, password):
        user = get_user_model().objects.create_user(
            username, '{}@wealize.digital'.format(username))
        user.set_password(password)
        user.save()

        return user
