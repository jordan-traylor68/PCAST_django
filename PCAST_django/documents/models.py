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
    name=models.CharField(max_length=500,null=False,blank=False)
    def __str__(self):
        return self.name