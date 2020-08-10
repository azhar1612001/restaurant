from django.urls import path
from .import views
urlpatterns=[
				path('',views.home,name='Home'),
				path('about',views.about,name='About Us'),
				path('menu',views.menu,name='Menu'),
				path('facility',views.facility,name='Banquet Facility'),
				path('gallery',views.gallery,name='Gallery'),
				path('catering',views.catering,name='Catering'),
				path('contact',views.contact,name='Contact'),
				path('booking',views.booking,name='Online Booking'),
				path('login',views.login,name='Login'),
				path('sinup',views.sinup,name='Sinup'),

]