from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html',{'passward':'tyuiuhhjih'})


def passward(request):
    thepassward = "testing"
    charecters =list('abdcefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
         charecters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
         if request.GET.get('spclchar'):
              charecters.extend(list('!@#$%^&*()'))
              if request.GET.get('numbers'):
                   charecters.extend(list('1234567890'))


    length = int(request.GET.get('length'))

    thepassward = ""
    for x in range(length):
        thepassward +=random.choice(charecters)
    return render(request,'generator/passward.html', {'passward':thepassward})
