from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(University)
admin.site.register(Grant)
admin.site.register(Faculty)
admin.site.register(Program)

