from django.contrib import admin

# Register your models here.
from .models import Student
from .models import User

admin.site.register(Student)
admin.site.register(User)