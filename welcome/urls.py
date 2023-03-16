from django.urls import path
from . import views

app_name = 'welcome'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('googlelogin/type/', views.selectTypeView.as_view(), name='selectType'),
    path('<str:id>/tutor/', views.tutorView.as_view(), name='tutor'),
    path('<str:id>/student/', views.studentView.as_view(), name='student'),
    path('finishSignup/', views.finishSignup, name='finishSignup'),
    path('selectClass/', views.selectClassView.as_view(), name = 'selectClass'),
    path('findClass/', views.findClass, name='findClass'),
<<<<<<< HEAD
    path('<int:user_id>/addToSchedule/', views.addToSchedule, name='addToSchedule')
=======
    path('<str:subject>/<str:catalog_nbr>/<str:descr>/tutorSignUp/', views.tutorSignUp, name='tutorSignUp'),
    path('findClassByName/', views.findClassByName, name='findClassByName')
>>>>>>> db4a9ada5c44a2e1dced1427bf0d79e06efec6f0
]