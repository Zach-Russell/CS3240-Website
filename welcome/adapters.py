from django.conf import settings
from django.urls import reverse
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
class MyAccountAdapter(DefaultAccountAdapter):
  def get_login_redirect_url(self, request):
      return '/googlelogin/type/'

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
  def get_login_redirect_url(self, request):
      return '/googlelogin/type/'