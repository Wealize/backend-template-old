from django.db.models.signals import post_save
from django.dispatch import receiver

from users.services import UserRegistrationService
from users.models import User


@receiver(post_save, sender=User)
def send_registration_password_confirm(sender, instance, created, **kwargs):
    if not created:
        return

    UserRegistrationService(instance).send_first_login_email()
