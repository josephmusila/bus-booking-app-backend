from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import  datetime
import jwt
from rest_framework.response import Response
from . import serializers
from rest_framework import generics
from . import models
from rest_framework.decorators import api_view
from django.template.loader import render_to_string
from django.core.mail import send_mail
from rest_framework import status
# Create your views here.


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        #find user using email
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Email Not Found')
            
        if not user.check_password(password):
            raise AuthenticationFailed('Invalid password')

       
        payload = {
            "id": user.id,
            "email": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        # token.decode('utf-8')
        #we set token via cookies
        

        response = Response() 
        queryset = User.objects.get(email = email)
        response.set_cookie(key='jwt', value=token, httponly=True)  #httonly - frontend can't access cookie, only for backend
        serializer = serializers.UserSerializer(queryset)
        # response.data = {
        #     'jwt token': token,
        #      "user":serializer.data,
        # }

        response.data=serializer.data

        #if password correct
        return response


class registerAPIView(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)   #if anything not valid, raise exception
        serializer.save()
        return Response(serializer.data)


class UpdateProfileView(generics.UpdateAPIView):
    queryset=models.User.objects.all()
   
    serializer_class=serializers.UserSerializer


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        app_token=request.headers.get("Authorization")
        print(app_token)
        print(token)

        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        
        try:
            payload = jwt.decode(token, 'secret', algorithms="HS256")
            #decode gets the user

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = serializers.UserSerializer(user)

        return Response(serializer.data)
        #cookies accessed if preserved

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'successful'
        }
        return response



@api_view(['POST'])
def reset_request(request):
    data=request.data
    email=data["email"]
    user=models.User.objects.get(email=email)

    if models.User.objects.filter(email=email).exists():
        msg_plain = render_to_string('base/base.html', {'otp': user.otp})
        msg_html = render_to_string('base/base.html', {'otp': user.otp})
        send_mail(
            "Password Reset",
            msg_plain,
            'info@vivatechy.com',
            [user.email],
            fail_silently=False,
            html_message=msg_html   
        )
        
        # send_sms(
        # f'Here is a message with {user.otp}.',
        # '0751218745',
        # ['0745787487'],
        # fail_silently=False
        # )

        message={
            "detail":"success message"
        }
        return Response(message,status=status.HTTP_200_OK)
    else:
        message = {
            "detail":"Email not found"
        }
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def reset_password(request):
    data=request.data
    user=models.User.objects.get(email=data['email'])
    new_password=data["password"]
    if user.is_active:
        if data['otp'] == user.otp:
            if new_password != "":
                user.set_password(data["password"])
                user.save()
                return Response({"message":"password updated"})
            else:
                message={
                    "detail":"Password cannot be empty"
                }
                return Response(message,status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {"detail":"Otp did not match"}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
    else:
        message = {"detail":"Something went wrong"}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
                