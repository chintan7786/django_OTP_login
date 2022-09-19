from django.shortcuts import render
from .models import User_Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        pass
    return render(request, 'account/register.html')