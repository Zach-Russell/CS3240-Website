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
    path('<int:user_id>/addToSchedule/', views.addToSchedule, name='addToSchedule'),
    path('<int:user_id>/viewTutorTime/', views.viewTutorTime, name='viewTutorTime'),
    path('<int:user_id>/<int:tutor_id>/<str:course>/requestTutorTime/', views.requestTutorTime, name='requestTutorTime'),
    path('findClassByName/', views.findClassByName, name='findClassByName'),
    path('selectTimings/', views.selectTimingsView.as_view(), name='selectTimings'),
    path('<int:user_id>/confirmTimings/', views.confirmTimings, name='confirmTimings'),
    path('<int:request_id>/requestChoice/', views.requestChoice, name='requestChoice'),
    path('<str:time_to_delete>/deleteTime', views.deleteTime, name='deleteTime')
]