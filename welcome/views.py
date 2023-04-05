from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import requests
from .models import User, Schedule, Request
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
    context_object_name = 'requests_list'
    def get_queryset(self):
        return Request.objects.all()

class studentView(generic.ListView):
    template_name = 'welcome/student.html'
    context_object_name = 'requests_list'
    def get_queryset(self):
        return Request.objects.all()

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
            schedule = Schedule(schedule = [], tutorTimings = [], User = user)
            schedule.save()
        list = request.POST.getlist('class')
        for x in list:
            if(x not in schedule.schedule):
                schedule.schedule.append(x)
                schedule.save()            
        url = '/' + user.email
        if(user.type == 'stu'):
            url += '/student/'
        else:
            url +='/tutor/'
        return HttpResponseRedirect((url))
    else:
        classReq = request.POST['class']
        schedules = Schedule.objects.filter(schedule__icontains=request.POST['class'])
        return render(request,'welcome/listTutors.html',{'schedules' : schedules, 'classReq': classReq})

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

# def tutorSignUp(request, subject, catalog_nbr, descr):
#     model = User
#     identifier = subject + ' ' + catalog_nbr + ': ' + descr
#     if(identifier not in model.classes_signed_up):
#         model.classes_signed_up.add(identifier)
#     user = request.user
#     url = '/' + user.email + '/tutor/'
#     return HttpResponseRedirect(url)

def findClassByName(request):
    courseName = request.POST['crsName']
    apiUrl = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&keyword=' + courseName
    courses = requests.get(apiUrl).json()
    res = []
    for course in courses:
        res.append(course)
    return render(request,'welcome/listClasses.html',{'classesFiltered' : res})

class selectTimingsView(generic.ListView):
    template_name = 'welcome/selectTimings.html'
    def get_queryset(self):
        return "timings success"

def viewTutorTime(request, user_id):
     spl = request.POST.get('tutor').split(' ')
     tutorId = spl[0]
     course = spl[1] + ' ' + spl[2]
     tutorUser = User.objects.get(pk=tutorId)
     tutorSchedule = Schedule.objects.get(User = tutorUser)
     tutorAvailableTimes = tutorSchedule.tutorTimings
     return render(request,'welcome/viewTutorTime.html',{'tutorUser' : tutorUser, 'tutorAvailableTimes' : tutorAvailableTimes, 'course': course})
     
def requestTutorTime(request, user_id, tutor_id, course):
    tutorUser = User.objects.get(pk=tutor_id)
    tutorSchedule = Schedule.objects.get(User=tutorUser)
    time = request.POST.get('tutorTime')
    user = User.objects.get(pk=user_id)
    request = Request(student = user, tutor = tutorUser, course = course, time = time)
    request.save()
    url = '/' + user.email
    if(user.type == 'stu'):
        url += '/student/'
    else:
        url +='/tutor/'
    return HttpResponseRedirect((url))

def confirmTimings(request, user_id):
    user = User.objects.get(pk=user_id)
    list = request.POST.getlist('class')
    for timing in list:
        spl = timing.split(' ')
        print(spl)
        day = spl[0]
        time = spl[1] + spl[2]
        course_time = day + ' ' + time
        try:
            schedule = Schedule.objects.get(User = user)
        except:
            schedule = Schedule(schedule = [], tutorTimings = [], User = user)
            schedule.save()
        if(course_time not in schedule.tutorTimings):
            schedule.tutorTimings.append(course_time)
        schedule.save()
    url = '/' + user.email
    if(user.type == 'stu'):
        url += '/student/'
    else:
        url +='/tutor/'
    return HttpResponseRedirect((url))

def requestChoice(request, request_id):
    req = Request.objects.get(pk = request_id)
    choice = request.POST.get('choice')
    if choice == 'accept':
        req.accepted='acc'
    else:
        req.accepted = 'dec'
    req.save()
    url = '/' + request.user.email
    if(request.user.type == 'stu'):
        url += '/student/'
    else:
        url +='/tutor/'
    return HttpResponseRedirect((url))

def deleteTime(request, time_to_delete):
    user = request.user
    schedule = Schedule.objects.get(User = user)
    schedule.tutorTimings.remove(time_to_delete)
    schedule.save()
    url = '/' + request.user.email
    if(request.user.type == 'stu'):
        url += '/student/'
    else:
        url +='/tutor/'
    return HttpResponseRedirect((url))