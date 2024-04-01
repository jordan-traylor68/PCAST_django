from django.contrib import admin
from documents.models import *
from namedEntities.models import PersonDocumentRelation,InstitutionDocumentRelation
import nested_admin

# def set_administration_ghwb(ModelAdmin, request, queryset):
#     administration = Administration.objects.get(name='George H.W. Bush Administration (1989-1993)')
#     for document in queryset:
#         Document.administration = administration
#         Document.save()

# def set_administration_wjc(ModelAdmin, request, queryset):
#     administration = Administration.objects.get(name='Bill Clinton Administration (1993-2001)')
#     for document in queryset:
#         Document.administration = administration
#         Document.save()

# def set_administration_gwb(ModelAdmin, request, queryset):
#     administration = Administration.objects.get(name='George W. Bush Administration (2001-2009)')
#     for document in queryset:
#         Document.administration = administration
#         document.save()

# def set_administration_bho(ModelAdmin, request, queryset):
#     administration = Administration.objects.get(name='Barack Obama Administration (2009-2017)')
#     for document in queryset:
#         Document.administration = administration
#         document.save()

# def set_administration_djt(ModelAdmin, request, queryset):
#     administration = Administration.objects.get(name='Donald J. Trump Administration (2017-2021)')
#     for document in queryset:
#         Document.administration = administration
#         document.save()

# def set_administration_jrb(ModelAdmin, request, queryset):
#     administration = Administration.objects.get(name='Joseph R. Biden Administration (2021-)')
#     for document in queryset:
#         Document.administration = administration
#         document.save()

# # def set_document_genre(ModelAdmin, request, queryset):
# #     documentgenre = DocumentGenre.objects.get(name=)

# set_administration_ghwb.short_description = "Set Administration to George H.W. Bush Administration"
# set_administration_wjc.short_description = "Set Administration to Bill Clinton Administration"
# set_administration_gwb.short_description = "Set Administration to George W. Bush Administration"
# set_administration_bho.short_description = "Set Administration to Barack Obama Administration"
# set_administration_djt.short_description = "Set Administration to Donald Trump Administration"
# set_administration_jrb.short_description = "Set Administration to Joe Biden Administration"


class PersonDocumentRelationInline(nested_admin.NestedStackedInline):
	model=PersonDocumentRelation
	classes = ['collapse']
	autocomplete_fields=['person']
	fields=['person','document','role','as_member_of']
	extra=0

class InstitutionDocumentRelationInline(nested_admin.NestedStackedInline):
	model=InstitutionDocumentRelation
	classes = ['collapse']
	autocomplete_fields=['institution']
	fields=['institution','document','role','part_of']
	extra=0

class DocumentAdmin(nested_admin.NestedModelAdmin):
    readonly_fields=['quartex_uid','quartex_name','asset_id']
    inlines=(
    	PersonDocumentRelationInline,
        InstitutionDocumentRelationInline
    )
    list_display=['title','quartex_name','asset_id','administration']
    search_fields=['title','asset_id','controlledsubjects']
    autocomplete_fields=['subjects','administration','documentgenre']
    # actions = [set_administration_bho,set_administration_djt,set_administration_ghwb,set_administration_gwb,set_administration_jrb,set_administration_wjc]


class LegacySubjectsAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name']
    readonly_display=['name']

class ControlledSubjectsAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name']

class AdministrationAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name']

class DocumentGenreAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name']


admin.site.register(Document,DocumentAdmin)
admin.site.register(LegacySubjects,LegacySubjectsAdmin)
admin.site.register(ControlledSubjects,ControlledSubjectsAdmin)
admin.site.register(Administration,AdministrationAdmin)
admin.site.register(DocumentGenre,DocumentGenreAdmin)
# admin.site.register(onquartex)
