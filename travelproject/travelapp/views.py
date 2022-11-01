from django.shortcuts import render
from .models import Place,State

# Create your views here.
def index(request):
    obj=Place.objects.all()
    obj1=State.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
