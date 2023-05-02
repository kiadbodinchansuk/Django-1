from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import datetime

def Greeting(request):
    current_datetime = datetime.datetime.now()  
    context={"current_datetime":current_datetime}
    return render(request,"index.html",{"context":context})