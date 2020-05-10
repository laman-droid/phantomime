from django.shortcuts import render
from django.http import HttpResponse
from .models import Show
from django.utils.translation import ugettext as _

# Create your views here.
def show(request):
    #sh = Show.objects.all()
    #output = ''.join([str(show.title + show.description) for show in sh])
    return render(request, 'index.html') #, {'out':output}
