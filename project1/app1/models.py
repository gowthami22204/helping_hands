from django.db import models

class Mycred(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    passcode = models.CharField(max_length=100)
    password = models.CharField(max_length=100,default='')
    is_Donar = models.BooleanField('Donar', null=False, default=False)
    is_Volunteer = models.BooleanField('Volunteer', null=False, default=False)
    is_Admin = models.BooleanField('Admin', null=False, default=False)
    is_Staff = models.BooleanField('Staff', null=False, default=False)
    roles = models.CharField(default='0',max_length=100)
    choice=(("1","medical camps"),("2","feed_needy"),("3","campaings"),("4","Amanuensis_scribe"),("5","animal_husbandry"),("6","others"))
    Areaofinterest=models.CharField(max_length=50,choices=choice,default="1")



# Authentication
class Login_out(models.Model):
    username = models.CharField(max_length=100)
    session_id = models.CharField(max_length=100)
    login_date = models.DateTimeField(auto_now_add=True)
    logout_date = models.DateTimeField(auto_now_add=True)

#usermodule
class  User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email= models.EmailField(max_length=100)

    
