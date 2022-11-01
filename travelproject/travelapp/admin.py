from django.contrib import admin

# Register your models here.
from .models import Place,State
admin.site.register(Place)
admin.site.register(State)