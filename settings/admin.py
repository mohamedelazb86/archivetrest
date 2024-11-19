from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Document_type,Sector

class SectorAdmin(SummernoteModelAdmin):
    list_display=['code','name']
    search_fields=['name','notes']
    summernote_fields = ('notes',)


class DocumentType(SummernoteModelAdmin):
    list_display=['code','name']
    search_fields=['name','notes']

    summernote_fields = ('notes',)


admin.site.register(Document_type,DocumentType)
admin.site.register(Sector,SectorAdmin)

