from django.contrib import admin

# Register your models here.
# posts/admin.py
from django.contrib import admin

from .models import DraftsModel



admin.site.register(DraftsModel)