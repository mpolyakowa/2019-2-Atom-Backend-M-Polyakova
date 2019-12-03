from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    print(request.user.id)
    return render(request, 'home.html')