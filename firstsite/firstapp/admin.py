from django.contrib import admin
from firstapp.models import Blog, User,Comment
# Register your models here.


admin.site.register(Blog)
admin.site.register(User)
admin.site.register(Comment)