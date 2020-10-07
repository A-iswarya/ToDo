from django.contrib import admin

#registering model with admin
from .models import ToDo
admin.site.register(ToDo);
