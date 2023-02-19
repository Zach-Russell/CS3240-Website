
from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login
@receiver(pre_social_login)
def get_data(request,sociallogin, **kwargs):
    print(sociallogin.user.email)