from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


#! signal oluştururken apps.py dosyasında UserConfig in içine/altına alttakini eklemez isek signal çalışmaz/onu görmez. O kodun anlamı "proje çalıştığında signalleri çalıştır" demek
"""
def ready(self):
    import users.signals
"""


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

