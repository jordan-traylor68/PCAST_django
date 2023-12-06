from django.contrib import admin
from namedEntities.models import *

# Register your models here.



class PersonAdmin(admin.ModelAdmin):
	list_display=['name','birth_year','death_year','wikipedia_grade']
	search_fields=['name']



admin.site.register(Person,PersonAdmin)
admin.site.register(Institution)
admin.site.register(Degree)
admin.site.register(Country)
admin.site.register(Ethnicity)
admin.site.register(AreaOfStudy)
admin.site.register(PersonDocumentRole)
admin.site.register(WikipediaGrade)