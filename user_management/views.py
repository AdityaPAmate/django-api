from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
import json



#create signup api
@csrf_exempt
def signup(request):
    #check the method is POST or not
    if request.method == 'POST':

        #convert the json to dictionary and store in one variable
        data= json.loads(request.body)

        #fetch the values of username and password and save in seperate variables
        username= data.get('username')
        password= data.get('password')

        # check username already exists or not
        if User.objects.filter(username==username).exists():
            return  JsonResponse({
                'message': 'Username Already Exists'
            })

        #store the data into user table which inbuilt in sqlite database
        User.objects.create_user(
            username = username,
            password = password
        )

        #return response as User Created successfully
        return JsonResponse({
            'message' : 'User Created Successfully'
        })

    return JsonResponse({
        'message': 'Only POST Request is Allowed'
    })

#create login api
from django.contrib.auth import authenticate
@csrf_exempt
def login_view(request):
    #check if request is post or not
    if request.method == 'POST':

        #convert the json into dictionary and store in variable
        data= json.loads(request.body)

        #extract and store the username and password values in different variable
        username = data.get('username')
        password = data.get('password')

        #authenticate it and return User Object otherwise None
        user = authenticate(
            username=username,
            password=password
        )

        #check if user contain User Object or not
        if user :
            return  JsonResponse ({
                'message' : 'Login Successfully'
            })
        else:
            return  JsonResponse({
                'message' : 'Invalid Username or Password'
            })

    return  JsonResponse({
        'message': 'Only POST Request is Allowed'
    })










