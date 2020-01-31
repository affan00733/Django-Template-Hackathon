from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):

    context = {
        "data" : "Template Django Project",
    }

    return render(request,'home/home.html',context)