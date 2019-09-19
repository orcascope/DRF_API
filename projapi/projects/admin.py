from django.contrib import admin

# Register your models here.
from .models import FA, Projects

admin.site.register(FA)
admin.site.register(Projects)
