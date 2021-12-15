import json

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from project.base import BaseTestCase
from users.services import URLService


class URLServiceTestCase(BaseTestCase):
    def test_get_url_base_localhost(self):

        url_base = URLService(
            ['localhost'], is_debug=True
        ).get_base_url()

        self.assertEqual(url_base, 'http://localhost')

    def test_get_url_base_production(self):

        url_base = URLService(
            ['backend.heroku.com'], is_debug=False
        ).get_base_url()

        self.assertEqual(url_base, 'https://backend.heroku.com')

    def test_get_absolute_url_localhost(self):

        url_base = URLService(
            ['localhost'], is_debug=True
        ).get_absolute_url('admin_password_reset', {})

        self.assertEqual(
            url_base,
            'http://localhost/admin/password_reset/'
        )

    def test_get_absolute_url_production(self):

        url_base = URLService(
            ['backend.heroku.com'], is_debug=False
        ).get_absolute_url('admin_password_reset', {})

        self.assertEqual(
            url_base,
            'https://backend.heroku.com/admin/password_reset/')


    def test_get_absolute_url_registration_link(self):
        user1_token = PasswordResetTokenGenerator().make_token(self.user1)
        uidb64 = urlsafe_base64_encode(force_bytes(self.user1.id))

        absolute_url = URLService(
            ['backend.heroku.com'], is_debug=False
        ).get_absolute_url(
            'password_reset_confirm',
            dict(uidb64=uidb64,
                 token=user1_token))

        self.assertEqual(
            absolute_url,
            f'https://backend.heroku.com/reset/{uidb64}/{user1_token}/')
