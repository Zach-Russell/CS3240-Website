from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import requests
from .models import User
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
        return "tutor success"

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

def tutorSignUp(request, subject, catalog_nbr, descr):
    model = User
    identifier = subject + ' ' + catalog_nbr + ': ' + descr
    if(identifier not in model.classes_signed_up):
        model.classes_signed_up.add(identifier)
    user = request.user
    url = '/' + user.email + '/tutor/'
    return HttpResponseRedirect(url)

def findClassByName(request):
    courseName = request.POST['crsName']
    apiUrl = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&keyword=' + courseName
    courses = requests.get(apiUrl).json()
    res = []
    for course in courses:
        res.append(course)
    return render(request,'welcome/listClasses.html',{'classesFiltered' : res})