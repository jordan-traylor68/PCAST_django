from django.db import models

# Create your models here.

class Document(models.Model):
	title=models.CharField(max_length=500,null=False,blank=False)
	asset_id=models.IntegerField(null=False,blank=False,unique=True)
	quartex_uid=models.CharField(max_length=36,null=False,blank=False,unique=True)
	quartex_name=models.CharField(max_length=100,null=False,blank=False,unique=True)
	lang=models.CharField(max_length=3,null=True,blank=True,unique=False)
	subjects=models.ManyToManyField('LegacySubjects')
	newsubjects=models.ManyToManyField('NewSubjects')
	documentgenre=models.ForeignKey('DocumentGenre',null=True,blank=True,on_delete=models.SET_NULL)
	administration=models.ForeignKey('Administration',models.SET_NULL,blank=True, null=True)
	def __str__(self):
		return self.title

class LegacySubjects(models.Model):
	name=models.CharField(max_length=500,null=False,blank=True,unique=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural="Legacy Subjects"

class Pages(models.Model):
	quartex_image_iiif_hash=models.CharField(max_length=36,null=False,blank=False,unique=True)
	document=models.ForeignKey(Document,null=False,blank=False,on_delete=models.CASCADE)
	order=models.IntegerField(null=False,blank=False)
	class Meta:
		unique_together = ["order", "document"]

class NewSubjects(models.Model):
	name=models.CharField(max_length=500,null=False,blank=True,unique=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural="Subjects"
class Administration(models.Model):
	controlled_name=models.CharField(
		max_length=100,
		null=True,
		blank=True,
		unique=True
	)
	class Meta:
		verbose_name_plural="Administrations"
	def __str__(self):
		return self.controlled_name

# Document genre: new field to describe document genre with Getty AAT vocabulary
class DocumentGenre(models.Model):
	name=models.CharField(max_length=500,null=True,blank=False,unique=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural="Document Genres"