from django.urls import path 
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('booking/',booking,name='booking'),
    path('history/',history,name='history'),
    path('support/',support,name='support'),
    path('about/',about,name='about'),
    path('booking_form/<int:id>',booking_form,name='booking_form'),
    path('update_booking/<int:id>',update_booking,name='update_booking'),
    path('cancel_booking/<int:id>',cancel_booking,name='cancel_booking')
]
