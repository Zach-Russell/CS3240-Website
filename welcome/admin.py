from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Schedule, Request

class ScheduleInLine(admin.TabularInline):
    model = Schedule

class RequestStudentInLine(admin.TabularInline):
    model = Request
    fk_name = 'student'

class RequestTutorInLine(admin.TabularInline):
    model = Request
    fk_name = 'tutor'
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name','last_name', 'last_login','type')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    inlines = [ScheduleInLine,RequestStudentInLine,RequestTutorInLine]

    list_display = ('email', 'first_name','last_name','type', 'is_staff', 'last_login')
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)