from django.contrib import admin
from .models import Profile, Student, Test

admin.site.register(Student)
admin.site.register(Test)
admin.site.register(Profile)

# Register your models here.
