from django.shortcuts import render
from django.conf import settings

# Create your views here.

def home_screen_view(request,*args,**kwargs):
    context = {'debug_mode': settings.DEBUG, 'room_id': "1"}
    return render(request, "personal/home.html", context)
