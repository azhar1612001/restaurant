from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'vegas/home.html')

def about(request):
	return render(request,'vegas/about.html')

def menu(request):
	return render(request,'vegas/menu.html')

def facility(request):
	return render(request,'vegas/facility.html')

def gallery(request):
	return render(request,'vegas/gallery.html')

def catering(request):
	return render(request,'vegas/catering.html')

def contact(request):
	return render(request,'vegas/contact.html')

def booking(request):
	return render(request,'vegas/booking.html')

def login(request):
	return render(request,'vegas/login.html')

def sinup(request):
	return render(request,'vegas/sinup.html')