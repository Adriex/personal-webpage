# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Social(models.Model):
    name = models.CharField(max_length=30,verbose_name="Nombre")
    link = models.CharField(max_length=2000,verbose_name="Link")
    fA_brand = models.CharField(max_length=30, verbose_name="FontAwesome Icon")
    fA_bkColor = models.CharField(max_length=30, verbose_name="FontAwesome Background Color")
    fA_size = models.CharField(max_length=30, verbose_name="FontAwesome Size", default="fa-2x")
    show = models.BooleanField(default=True,blank=True)

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
    def __str__(self):
        tagName = str(self.name)
        return tagName

@python_2_unicode_compatible
class Link(models.Model):
    idLink = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, name="Title")
    link = models.CharField(max_length=2000, blank=True)
    video = models.BooleanField(blank=True)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
    def __str__(self):
        tagName = str(self.Title)+'['+str(self.idLink)+"]"
        return tagName

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=128, primary_key=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    def __str__(self):
        tagName = str(self.name)
        return tagName

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=128, primary_key=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    def __str__(self):
        tagName = str(self.name)
        return tagName

@python_2_unicode_compatible
class Entry(models.Model):
    idEntry = models.AutoField(primary_key=True)
    publish = models.BooleanField(default=True,blank=True)
    title = models.CharField(max_length=30)
    dateEntry = models.DateField()
    content = HTMLField() #From tinymce
    idLinks = models.ManyToManyField(Link)
    idCategory = models.ForeignKey(Category, blank=True)
    idTags = models.ManyToManyField(Tag)
    autor = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
    def __str__(self):
        tagName = str(self.title)+'['+str(self.dateEntry)+"]"+"("+str(self.idCategory.name)+")"
        return tagName
