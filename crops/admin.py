import csv

from datetime import datetime, date
from django.contrib import admin
from django.http import HttpResponse
from django.utils.encoding import smart_str
from . import models


def export_csv(modeladmin, request, queryset):
    dt = datetime.now()
    d = date(dt.year, dt.month, dt.day)
    file_name = 'crop-export-{0}.csv'.format(d)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(file_name)
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # Excel needs this
    writer.writerow([
        smart_str(u'ID'),
        smart_str(u'Name'),
        smart_str(u'Category'),
        smart_str(u'Tier'),
        smart_str(u'Transplant'),
        smart_str(u'Direct Seed'),
        smart_str(u'Start Date'),
        smart_str(u'End Date')
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.name),
            smart_str(obj.category),
            smart_str(obj.tier),
            smart_str(obj.transplant),
            smart_str(obj.direct_seed),
            smart_str(obj.plant_start_date),
            smart_str(obj.plant_end_date)
        ])
    return response


class CropAdmin(admin.ModelAdmin):
    actions = [export_csv]
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)


admin.site.register(models.Crop, CropAdmin)
admin.site.register(models.Category)
