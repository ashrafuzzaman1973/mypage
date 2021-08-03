from travello.models import Destination
from django.shortcuts import render

# Create your views here.

def index(request):
    des1 = Destination()
    des1.name = 'Dhaka'
    des1.desc = 'This city never sleep'
    des1.image = 'destination_1.jpg'
    des1.price = 700
    des1.offer = False

    des2 = Destination()
    des2.name = 'Chittagong'
    des2.desc = 'This city of beach'
    des2.image = 'destination_2.jpg'
    des2.price = 750
    des2.offer = True

    des3 = Destination()
    des3.name = 'Rangpur'
    des3.desc = 'This city of silent'
    des3.image = 'destination_3.jpg'
    des3.price = 650
    des3.offer = False

    dests = [des1,des2,des3]
    return render(request,'index.html',{'dests':dests})
