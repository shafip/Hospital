from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
class AdminDepartment(admin.ModelAdmin):
    list_display = ('de_description','de_name','image')
admin.site.register(Department,AdminDepartment)

class AdminModel(admin.ModelAdmin):
    list_display = ('ID','department','name','image')
admin.site.register(DoctorIn,AdminModel)


class AdminToken(admin.ModelAdmin):
    list_display = ('Token_id','date','Fullname','Email','Phone','Age','Department','Doctor')
admin.site.register(Booking,AdminToken)

