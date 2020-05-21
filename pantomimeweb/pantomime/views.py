from django.shortcuts import render
from django.http import HttpResponse
from .models import Nowshow, Upcomingshow
from django.utils.translation import ugettext as _

# Create your views here.
def shows(request):
    nowshows = Nowshow.objects.all()
    upcomingshows = Upcomingshow.objects.all()
    return render(request, 'index.html', {'nowshows':nowshows, 'upcomingshows':upcomingshows})
