#coding: utf-8

from django.db import models
from sorl.thumbnail import ImageField

class Category(models.Model):
	key = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	image = ImageField(upload_to='category', null=True)
	def __unicode__(self):
		return self.name

class Reccomendation(models.Model):
	name = models.CharField("Заголовок",max_length=200)
	image = ImageField(upload_to='reccomendation', null=True)
	about = models.TextField("Описание", blank=True)
	appstore = models.URLField("Аппстор", blank=True)
	google = models.URLField("Гугл Плэй", blank=True)
	youtube = models.URLField("Ютуб", blank=True)
	link = models.URLField("Ссылка", blank=True)

	category = models.ManyToManyField(Category)
	pubDate = models.DateTimeField("Дата публикации", auto_now_add = True)

	def __unicode__(self):
		return self.name

