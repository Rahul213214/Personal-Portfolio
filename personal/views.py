from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    main_name={'fname':'Rahul','lname':'Dalvi'}
    return render(request,'index.html',main_name)