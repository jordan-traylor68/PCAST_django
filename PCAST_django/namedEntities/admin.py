from django.contrib import admin
from namedEntities.models import *
from documents.models import *
import nested_admin
from django.utils.html import format_html

# Register your models here.

def set_sector_fg(ModelAdmin, request, queryset):
	sector = Sector.objects.get(name='Federal government')
	for Institution in queryset:
		Institution.sector = sector
		Institution.save()

def set_sector_sg(ModelAdmin, request, queryset):
	sector = Sector.objects.get(name='State government')
	for Institution in queryset:
		Institution.sector = sector
		Institution.save()

def set_sector_lg(ModelAdmin, request, queryset):
	sector = Sector.objects.get(name='Local government')
	for Institution in queryset:
		Institution.sector = sector
		Institution.save()

def set_sector_ps(ModelAdmin, request, queryset):
	sector = Sector.objects.get(name='Private sector')
	for Institution in queryset:
		Institution.sector = sector
		Institution.save()

def set_sector_ns(ModelAdmin, request, queryset):
	sector = Sector.objects.get(name='Nonprofit sector')
	for Institution in queryset:
		Institution.sector = sector
		Institution.save()

def set_sector_ac(ModelAdmin, request, queryset):
	sector = Sector.objects.get(name='Academia')
	for Institution in queryset:
		Institution.sector = sector
		Institution.save()

def set_sector_mi(ModelAdmin, request, queryset):
	sector = Sector.objects.get(name='Military')
	for Institution in queryset:
		Institution.sector = sector
		Institution.save()

def set_sector_for(ModelAdmin, request, queryset):
	sector = Sector.objects.get(name='Foreign government')
	for Institution in queryset:
		Institution.sector = sector
		Institution.save()		

set_sector_fg.short_description = "Set sector to Federal government"
set_sector_sg.short_description = "Set sector to State government"
set_sector_lg.short_description = "Set sector to Local government"
set_sector_ps.short_description = "Set sector to Private sector"
set_sector_ns.short_description = "Set sector to Nonprofit sector"
set_sector_ac.short_description = "Set sector to Academia"
set_sector_mi.short_description = "Set sector to Military"
set_sector_for.short_description = "Set sector to Foreign government"

class PersonDocumentInline(nested_admin.NestedStackedInline):
	model=PersonDocumentRelation
	classes = ['collapse']
	extra=0

class PersonAdmin(nested_admin.NestedModelAdmin):
	inlines=(
		PersonDocumentInline,
	)
	list_display=['name','birth_year','death_year','wikipedia_grade']
	search_fields=['name']
	change_form_template = "admin/namedEntities/person/change_form.html"

	def change_view(self, request, object_id, form_url='', extra_context=None):
		# Fetch the person object
		person = self.get_object(request, object_id)

		# Count related documents using PersonDocumentRelation
		document_count = PersonDocumentRelation.objects.filter(person=person).count()

		# Prepare the extra context
		extra_context = extra_context or {}
		extra_context['document_count_text'] = format_html(
			"<div><strong>This person appears in {} documents.</strong></div>",
			document_count
		)

		return super().change_view(request, object_id, form_url, extra_context=extra_context)





class InstitutionAdmin(admin.ModelAdmin):
	list_display=['name','sector']
	actions = [set_sector_fg,set_sector_ac,set_sector_lg,set_sector_ns,set_sector_ps,set_sector_sg,set_sector_mi,set_sector_for]
	search_fields=['name']

admin.site.register(Person,PersonAdmin)
admin.site.register(Institution,InstitutionAdmin)
admin.site.register(Degree)
admin.site.register(Country)
admin.site.register(Ethnicity)
admin.site.register(AreaOfStudy)
admin.site.register(PersonDocumentRole)
admin.site.register(InstitutionDocumentRole)
admin.site.register(WikipediaGrade)
admin.site.register(Sector)