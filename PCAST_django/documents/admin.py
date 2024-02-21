from django.contrib import admin
from documents.models import *
from namedEntities.models import PersonDocumentRelation
import nested_admin

class PersonDocumentRelationInline(nested_admin.NestedStackedInline):
	model=PersonDocumentRelation
	classes = ['collapse']
	autocomplete_fields=['person']
	fields=['person','document','role','as_member_of']
	extra=0

class DocumentAdmin(nested_admin.NestedModelAdmin):
    readonly_fields=['quartex_uid','quartex_name','asset_id']
    inlines=(
    	PersonDocumentRelationInline,
    )
    list_display=['title','quartex_name','asset_id','administration']
    search_fields=['title','asset_id']
    autocomplete_fields=['subjects','newsubjects','administration','documentgenre']

class LegacySubjectsAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name']
    readonly_display=['name']

class NewSubjectsAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name']

class AdministrationAdmin(admin.ModelAdmin):
    search_fields=['controlled_name']
    list_display=['controlled_name']

class DocumentGenreAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name']

admin.site.register(Document,DocumentAdmin)
admin.site.register(LegacySubjects,LegacySubjectsAdmin)
admin.site.register(NewSubjects,NewSubjectsAdmin)
admin.site.register(Administration,AdministrationAdmin)
admin.site.register(DocumentGenre,DocumentGenreAdmin)
