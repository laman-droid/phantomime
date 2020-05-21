from django.contrib import admin
from .models import Nowshow, Upcomingshow

# Register your models here.

admin.site.register(Nowshow)
admin.site.register(Upcomingshow)

