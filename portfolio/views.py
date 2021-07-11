from django.shortcuts import render
from .models import Project
# Create your views here.


def portfolio_main(request):
    portlist = Project.objects.all()
    return render(request, 'portfolio_main.html', {'portlist': portlist})