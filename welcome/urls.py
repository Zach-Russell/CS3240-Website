from django.urls import path
from . import views

app_name = 'welcome'
urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.SigninView.as_view(),name = 'signin'),
    path('signinAction/', views.signin,name = 'signinAction')
]