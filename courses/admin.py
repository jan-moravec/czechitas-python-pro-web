from django.contrib import admin
from . import models


admin.site.register(models.Course)
admin.site.register(models.Branch)
admin.site.register(models.People)
admin.site.register(models.Category)
admin.site.register(models.Application)
