from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.

def index(request):
    return render(request, 'apptwo/index.html')


def users(request):
    # THIS AINT WORKING
    return render(request, 'apptwo/users.html')
