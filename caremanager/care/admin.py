from django.contrib import admin

# Register your models here.
from care.models import MediaclRecord,UserUni

admin.site.register(MediaclRecord)
admin.site.register(UserUni)