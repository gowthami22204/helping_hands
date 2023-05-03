from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import  APIView
from .models import Mycred
from .serializers import SignupSerializer, SetPasswordSerializer, LoginSerializer, ViewProfile,ProfileUpdate
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.contrib.auth import logout
from django.conf import settings
from django.http import request
from django.core.mail import send_mail
import random
import string


# Create your views here.


def passcode():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(6))
    print("Random password is:", password)
    return password


class SignUpView(generics.CreateAPIView):
    queryset = Mycred.objects.all()
    serializer_class = SignupSerializer

    def post(self, request):
        print(request.data, 'inside post')

        data = request.data.copy()
        otp = passcode()
        data['passcode'] = otp


        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() # Add this line to save the record

        # Update the roles field based on the is_Volunteer flag
        if user.is_Donar:
            Mycred.objects.filter(pk=user.pk).update(roles=3) # Add this line to save the record
        elif user.is_Volunteer:
            Mycred.objects.filter(pk=user.pk).update(roles=4)
        elif user.is_Admin:
            Mycred.objects.filter(pk=user.pk).update(roles=1)
        elif user.is_Staff:
            Mycred.objects.filter(pk=user.pk).update(roles=2)
        elif user.is_Organizer:
            Mycred.objects.filter(pk=user.pk).update(roles=1)

        # smtp passcode
        # print(data['email'])
        # subject = 'Passcode Verification code'
        # message = f'Hi, your passcode: {otp}. Thanks for registering with Helping Hands...'
        # sender = settings.EMAIL_HOST_USER
        # recipant=[data['email'],]
        # send_mail(subject, message, sender,recipant )

        return Response({'success': 'Registration Successful !!!'}, status=status.HTTP_200_OK)
    
class SetPassword(generics.UpdateAPIView):
    queryset = Mycred.objects.all()
    serializer_class = SetPasswordSerializer

    def put(self, request):
        name = request.data.get('username')
        passcode = request.data.get('passcode')
        print(request.user)
        print(name, passcode)
        obj = Mycred.objects.get(username=name)
        print(obj)
        # serializer = SetPasswordSerializer(obj, data=request.data, partial=True)
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"success": 'password setup successful...'}, status=status.HTTP_201_CREATED)
        return Response({"error": 'password not setup ...'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        print('data:', username, password)
        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = Mycred.objects.get(username=username, password=password)
        print('user:->', user)
        if not user:
            return Response({'error': 'Invalid email or passcode'}, status)
        else:
            return Response({"success": 'login successful...'})
        

class volunteerProfile(generics.RetrieveAPIView):
    queryset=Mycred.objects.all()
    serializer_class = ViewProfile
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        print(request.data, 'inside post')
        
    def create_object(self):
        return self.request.user
    

class ProfileUpdate(generics.UpdateAPIView):
    serializer_class = ProfileUpdate
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    def perform_update(self, serializer):
        serializer.save()

# logout the user and clear their session data

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        request.session.flush()
        return Response({"message": "Logout successful"})


logout
class LogoutView(generics.CreateAPIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Logged out successfully.'})


#volunteer dashboard

# class VolunteerDashboardView(generics.RetrieveAPIView):
#     serializer_class = VolunteerDashboardSerializer
#     permission_classes = (IsAuthenticated,)
    
#     def get_object(self):
#         return self.request.user
    
#     def retrieve(self, request, *args, **kwargs):
#         user = self.get_object()
        
#         # Get the user's role
#         role = Mycred.objects.get(pk=user.pk).roles
        
#         # Get the user's tasks based on their role
#         if role == 4: # Volunteer
#             tasks = user.objects.filter(volunteer=user)
#         else:
#             tasks = user.objects.filter(assigned_to=user)
        
#         serializer = self.get_serializer({'tasks': tasks})
        
#         return Response(serializer.data)

