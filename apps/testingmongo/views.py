from django.shortcuts import render
from apps.testingmongo.models import Poll, Choice
from mongoengine import *
from apps.testingmongo.models import *
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth import authenticate
from django.http import *
from django.contrib.auth import login,  logout
import datetime
# Create your views here.


def save_data(request):
	object_var = Choice()
	object_var.choice_text = "testing data "
	object_var.votes = 10
	object_poll = Poll()
	object_poll.question = "I love SRM University"
	object_poll.pub_date = datetime.datetime.now()
	object_poll.choices.append(object_var)
	object_poll.save()

	for poll in Poll.objects:
		print poll.question
	variable_shit = Poll.objects.filter(question__icontains= "h").first()
	variable_shit.question = "i changed the question"
	variable_shit.save()
	print variable_shit
	return HttpResponse ("it worked")

def save_user(request):
	object_user = User()
	object_user.username = "digu35"
	object_user.first_name = "subham"
	object_user.last_name = "bal"
	object_user.email = "digu35@gmail.com"
	hasher = PBKDF2PasswordHasher()
	object_user.password = hasher.encode(password= 'admin' , salt='salt',iterations= 50000)
	object_user.last_login = datetime.datetime.now()
	object_user.date_joined = datetime.datetime.now()
	object_user.save()
	return HttpResponse("user saved")

def login_setup (request):
	user = authenticate(username='digu35', password='admin')
	print user
	login(request, user)
	print request.user.username
	print request.user.id
	print request.user.is_authenticated()
	return HttpResponse('user logged in')

def logged_user(request):
	return HttpResponse(request.user.username)