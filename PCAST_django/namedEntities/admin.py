from django.contrib import admin
from namedEntities.models import *

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

set_sector_fg.short_description = "Set sector to Federal government"
set_sector_sg.short_description = "Set sector to State government"
set_sector_lg.short_description = "Set sector to Local government"
set_sector_ps.short_description = "Set sector to Private sector"
set_sector_ns.short_description = "Set sector to Nonprofit sector"
set_sector_ac.short_description = "Set sector to Academia"

class PersonAdmin(admin.ModelAdmin):
	list_display=['name','birth_year','death_year','wikipedia_grade']
	search_fields=['name']

class InstitutionAdmin(admin.ModelAdmin):
	list_display=['name','sector']
	actions = [set_sector_fg,set_sector_ac,set_sector_lg,set_sector_ns,set_sector_ps,set_sector_sg]

admin.site.register(Person,PersonAdmin)
admin.site.register(Institution,InstitutionAdmin)
admin.site.register(Degree)
admin.site.register(Country)
admin.site.register(Ethnicity)
admin.site.register(AreaOfStudy)
admin.site.register(PersonDocumentRole)
admin.site.register(WikipediaGrade)
admin.site.register(Sector)