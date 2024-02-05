from django.db import models
from documents.models import Document
# Create your models here.

# STATUS_CHOICES = {
#     "fg": "Federal government"
# 	"sg": "State government"
# 	"lg": "Local government"
# 	"ps": "Private sector"
# 	"ns": "Nonprofit sector"
# 	"ac": "Academia"
# }

class Ethnicity(models.Model):
	controlled_name=models.CharField(
		max_length=255,
		null=False,
		blank=False,
		unique=True
	)
	class Meta:
		verbose_name_plural="Ethnicities"
	def __str__(self):
		return self.controlled_name


class Country(models.Model):
	controlled_name=models.CharField(
		max_length=255,
		null=False,
		blank=False,
		unique=True
	)
	class Meta:
		verbose_name_plural="Countries"
	def __str__(self):
		return self.controlled_name

class Degree(models.Model):
	controlled_name=models.CharField(
		max_length=255,
		null=False,
		blank=False,
		unique=True
	)
	def __str__(self):
		return self.controlled_name

class AreaOfStudy(models.Model):
	controlled_name=models.CharField(
		max_length=255,
		null=False,
		blank=False,
		unique=True
	)
	class Meta:
		verbose_name_plural="Areas of Study"
	def __str__(self):
		return self.controlled_name

# Sector: New field to categorize institutions by sector (public, private, etc.)
class Sector(models.Model):
	name=models.CharField(
		max_length=255,
		null=False,
		blank=False,
		unique=True
	)
	def __str__(self):
		return self.name

class Institution(models.Model):
	name=models.CharField(
		max_length=255,
		null=False,
		blank=False,
		unique=True
	)
	sector=models.ForeignKey(
		Sector,
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)
	def __str__(self):
		return self.name



# Wikipedia Grade: New field that should only be used for PCAST & OSTP members
class WikipediaGrade(models.Model):
	name=models.CharField(
		max_length=255,
		null=False,
		blank=False,
		unique=True
	)
	class Meta:
		verbose_name_plural="Wikipedia Grades"
	def __str__(self):
		return self.name
	
class PersonDocumentRole(models.Model):
	name=models.CharField(
		max_length=255,
		null=False,
		blank=False,
		unique=True
	)
	
	def __str__(self):
		return self.name	
	class Meta:
		verbose_name_plural="Person Document Roles"
		ordering=['id']

class PersonDocumentRelation(models.Model):
	person=models.ForeignKey(
		"Person",
		null=False,
		blank=False,
		on_delete=models.CASCADE
	)
	document=models.ForeignKey(
		Document,
		null=False,
		blank=False,
		on_delete=models.CASCADE
	)
	role=models.ForeignKey(
		PersonDocumentRole,
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)
	as_member_of=models.ForeignKey(
		Institution,
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)
	
class PersonPersonRelation(models.Model):
	alice=models.ForeignKey(
		"Person",
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name="person_relation_source"
	)
	bob=models.ForeignKey(
		"Person",
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name="person_relation_target"
	)
	notes=models.TextField(
		null=True,
		blank=True
	)
	document=models.ForeignKey(
		Document,
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)
	def __str__(self):
		return self.alice + self.bob






class Person(models.Model):
	
	name=models.CharField(
		"Name of person, canonical, unformatted",
		max_length=255,
		null=False,
		blank=False
	)
	country_of_origin=models.ForeignKey(
		Country,
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)
	birth_year=models.IntegerField(
		"Year of birth",
		null=True,
		blank=True
	)
	death_year=models.IntegerField(
		"Year of death",
		null=True,
		blank=True
	)
	ethnicity=models.ForeignKey(
		Ethnicity,
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)
	
	highest_degree=models.ForeignKey(
		Degree,
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)
	
	area_of_study=models.ForeignKey(
		AreaOfStudy,
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)
	area_of_expertise=models.CharField(
		max_length=255,
		null=True,
		blank=True
	)
	
	degree_granting_institution=models.ForeignKey(
		Institution,
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)

	wikipedia_grade=models.ForeignKey(
		WikipediaGrade,
		help_text="Please use for PCAST & OSTP members only.",
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)
	class Meta:
		verbose_name_plural="People"
		ordering=['id']
	def __str__(self):
		return self.name
