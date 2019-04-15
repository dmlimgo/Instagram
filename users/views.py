from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/list.html', context)