from django.contrib import admin
from .models import post , Profile , Like,Comment

# Register your models here.
admin.site.register(post)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Comment)


