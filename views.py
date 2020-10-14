from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name='Mumbai'
    dest1.price=1000
    dest1.desc='Visit the Gateway to India\'s heart'
    dest1.img='destination_3.jpg'

    dest2=Destination()
    dest2.name='Agra'
    dest2.img='destination_4.jpg'
    dest2.price=1200
    dest2.desc='Welcome to the one of the 7 wonders'

    dest3=Destination()
    dest3.name='Jaipur'
    dest3.price=900
    dest3.img='destination_5.jpg'
    dest3.desc='Padharo mare desh'

    dests=[dest1, dest2, dest3]


    return render(request,'index.html',{'dests':dests})

