from django.contrib import admin
from . import models


class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)


admin.site.register(models.Crop, CropAdmin)
admin.site.register(models.Category)
