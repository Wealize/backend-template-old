from typing import List

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from users.models import User


class URLService():
    def __init__(self, allowed_hosts: List, is_debug: bool):
        self.domain = allowed_hosts[0]
        self.is_debug = is_debug

    def get_absolute_url(self, name, arguments):
        base_url = self.get_base_url()
        path = reverse(name, kwargs=arguments)

        return f'{base_url}{path}'

    def get_base_url(self):
        protocol = 'http' if self.is_debug  else 'https'
        return f'{protocol}://{self.domain}'


class UserRegistrationService():
    def __init__(
        self,
        user: User,
        token_generator = PasswordResetTokenGenerator
    ):
        self.user = user
        self.token_generator = token_generator

    def send_first_login_email(self) -> None:
        user_token = self.token_generator().make_token(self.user)
        registration_url = URLService(
            settings.ALLOWED_HOSTS, settings.DEBUG
        ).get_absolute_url(
            'password_reset_confirm',
            dict(uidb64=urlsafe_base64_encode(force_bytes(self.user.id)),
                 token=user_token)
        )

        send_mail(
            'Bienvenido a Hermes',
            f'''
                Bienvenido a Hermes.

                Por favor, sigue el siguiente enlace para
                registrarte {registration_url}
            ''',
            settings.ADMIN_EMAIL,
            (self.user.email, ),
            fail_silently=False)
