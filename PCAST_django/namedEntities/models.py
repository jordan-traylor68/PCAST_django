from django.db import models
from document.models import Document
# Create your models here.

class Ethnicity(models.Model):
    controlled_name=models.CharField(
        "Ethnicity",
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )

class Country(models.Model):
    controlled_name=models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )

class Degree(models.Model):
    controlled_name=models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )

class AreaOfStudy(models.Model):
    controlled_name=models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )

class Institution(models.Model):
    name=models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )

class PersonDocumentRole(models.Model):
    name=models.CharField(
        null=False,
        blank=False,
        unique=True
    ) 

class PersonDocumentRelation(models.Model):
    person=models.ForeignKey(
        "Person",
        null=False,
        blank=False,
    )
    document=models.ForeignKey(
        Document,
        null=False,
        blank=False,
    )
    role=models.ForeignKey(
        PersonDocumentRole,
        null=False,
        blank=False
    )
    as_member_of=models.ForeignKey(
        Institution,
        null=True,
        blank=True
    )

class PersonPersonRelation(models.Model):
    alice=models.ForeignKey(
        "Person",
        null=False,
        blank=False,
    )
    bob=models.ForeignKey(
        "Person",
        null=False,
        blank=False,
    )
    notes=models.TextField(
        null=False,
        blank=False
    )
    document=models.ForeignKey(
        Document,
        null=False,
        blank=False,
    )

class Person(models.Model):
    controlled_name=models.CharField(
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
    death_date=models.IntegerField(
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

    area_of_exptertise=models.CharField(
        "Name of person, canonical, unformatted",
        max_length=255,
        null=False,
        blank=False
    )

    degree_granting_institution=models.ForeignKey(
        Institution,
        null=True,
        blank=True,
        on_delete=models.SET_NULL

    )