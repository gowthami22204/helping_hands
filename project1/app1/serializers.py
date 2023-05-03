from rest_framework import serializers
from .models import Mycred,User

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mycred
        fields = ['is_Donar','is_Volunteer','first_name','last_name','username','email','Areaofinterest']


class SetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mycred
        fields = ['username', 'passcode', 'password']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mycred
        fields = ['username', 'password']

#profile
class ViewProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['first_name','last_name','username','email']


#profile of donar
class ProfileUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['first_name','last_name','username','email']

#volunteerdashboard

# class VolunteerDashboardSerializer(serializers.Serializer):
#     tasks = LoginSerializer(many=True)
