from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import User
# Create your views here.


def index(request):
    return HttpResponse("Hello World! This is the team a25's welcome index.")

class SigninView(generic.ListView):
    model = User
    template_name = 'welcome/signin.html'
def signin(request):
    model = User
    try:
        username = request.POST['username']
        password = request.POST['password']
    except (KeyError, User.DoesNotExist):
        # Redisplay the comments voting form.
        return render(request, 'welcome/signin.html', {
            'User': User,
            'error_message': "Add all fields",
        })
    else:
        return HttpResponseRedirect(('/welcome'))