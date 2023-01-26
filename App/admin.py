from django.contrib import admin
from . models import (Blog , Tag , Category , Comment , SubComment)
# Register your models here.
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(SubComment)