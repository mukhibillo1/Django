from django.contrib import admin

from common import models


admin.site.register(models.Add)
admin.site.register(models.NewsTag)
admin.site.register(models.NewsCategory)
admin.site.register(models.Region)
admin.site.register(models.News)
