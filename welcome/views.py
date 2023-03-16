from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import requests
from .models import User, Schedule
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'welcome/index.html'
    def get_queryset(self):
        return "index success"

class selectTypeView(generic.ListView):
    template_name = 'welcome/selectType.html'
    def get_queryset(self):
        return "selectType success"

class tutorView(generic.ListView):
    template_name = 'welcome/tutor.html'
    def get_queryset(self):
        return "tutor_success"


class studentView(generic.ListView):
    template_name = 'welcome/student.html'
    def get_queryset(self):
        return "student success"

class selectClassView(generic.ListView):
    template_name = 'welcome/selectClasses.html'

    def get_context_data(self, **kwargs):
        url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearchOptions?institution=UVA01&term=1232'
        res = requests.get(url)
        resJson = res.json()
        context = super().get_context_data(**kwargs)
        context['subjects'] = resJson['subjects']
        return context
    def get_queryset(self):
        return 'select Class success'

def findClass(request):
    model = User
    try:
        crsSubject = request.POST['class']
    except (KeyError, User.DoesNotExist):
        return render(request, 'welcome/selectClasses.html', {
            'comments': User,
            'error_message': "Add all necessary fields",
        })
    url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&subject=' + crsSubject  + '&page=1'
    if request.POST['crsNum'] != "":
        url += '&catalog_nbr=' + request.POST['crsNum']
    classes = requests.get(url).json()
    seen = []
    classesFiltered = []
    for x in classes:
        if x['catalog_nbr'] not in seen:
            seen.append(x['catalog_nbr'])
            classesFiltered.append(x)
    return render(request,'welcome/listClasses.html',{'classesFiltered' : classesFiltered})

def addToSchedule(request, user_id):
    if request.user.type == 'tut':
        user = User.objects.get(pk = user_id)
        try:
            schedule = Schedule.objects.get(User = user)
        except Schedule.DoesNotExist:
            schedule = Schedule(schedule = [], User = user)
            schedule.save()
        list = request.POST.getlist('class')
        for x in list:
            schedule.schedule.append(x)
            schedule.save()            
        url = '/' + user.email
        if(user.type == 'stu'):
            url += '/student/'
        else:
            url +='/tutor/'
        return HttpResponseRedirect((url))
    else:
        schedules = Schedule.objects.filter(schedule__icontains=request.POST['class'])
        return render(request,'welcome/listTutors.html',{'schedules' : schedules})

def finishSignup(request):
    model = User
    try:
        choice = request.POST['type']
    except (KeyError, User.DoesNotExist):
        return render(request, 'welcome/selectType.html', {
            'comments': User,
            'error_message': "Add all fields",
        })
    else:
        user = request.user
        user.type = choice
        user.save()
        url = '/' + user.email
        if(user.type == 'stu'):
            url += '/student/'
        else:
            url +='/tutor/'
        return HttpResponseRedirect((url))