from django.contrib import admin
from documents.models import *
# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    readonly_fields=['quartex_uid','quartex_name','asset_id']
    list_display=['title','lang','asset_id']
    search_fields=['title','asset_id']
    autocomplete_fields=['subjects']

class LegacySubjectsAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name']
    readonly_display=['name']

admin.site.register(Document,DocumentAdmin)
admin.site.register(LegacySubjects,LegacySubjectsAdmin)