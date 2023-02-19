from django.db import models
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
class User(models.Model):
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)
    user_type = [
        'Tutor', 'Tutor',
        'Student', 'Student'
    ]
    def __str__(self):
        return self.first_name + " " + self.last_name
# Create your models here.


# @receiver(user_logged_in)
# def login_logger(request, user, **kwargs):
#     print('jaksdlfa;sdfjaklsdfjlkasdkjlfaskjld;fkjl;adskjl;faskjl;dfkjl;adskjlfkjlasdkjlfjlasnmcvnzx')