from django.contrib import admin
from .models import posts, auth_user, comments, reply

# Register your models here.
admin.site.register(posts)
admin.site.register(auth_user)
admin.site.register(comments)
admin.site.register(reply)


