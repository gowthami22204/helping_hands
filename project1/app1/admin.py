from django.contrib import admin
from .models import Mycred
# Register your models here.
@admin.register(Mycred)
class mycredentials(admin.ModelAdmin):
    list_display= ['is_Donar','is_Volunteer','first_name','last_name','username','email','passcode','password','Areaofinterest']
