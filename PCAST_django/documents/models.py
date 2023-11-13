from django.db import models

# Create your models here.

class Document(models.Model):
	title=models.CharField(max_length=500,null=False,blank=False)
	asset_id=models.IntegerField(null=False,blank=False,unique=True)
	quartex_uid=models.CharField(max_length=36,null=False,blank=False,unique=True)
	quartex_name=models.CharField(max_length=100,null=False,blank=False,unique=True)
	lang=models.CharField(max_length=3,null=True,blank=True,unique=False)
	subjects=models.ManyToManyField('LegacySubjects')
	def __str__(self):
		return self.title

class LegacySubjects(models.Model):
	name=models.CharField(max_length=500,null=False,blank=False,unique=True)
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