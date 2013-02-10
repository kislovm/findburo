#coding: utf-8

from django.db import models

class Category(models.Model):
	key = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name

class Reccomendation(models.Model):
	name = models.CharField("Заголовок",max_length=200)
	about = models.TextField("Описание")
	appstore = models.URLField("Аппстор")
	google = models.URLField("Гугл Плэй")
	youtube = models.URLField("Ютуб")
	link = models.URLField("Ссылка")

	category = models.ManyToManyField(Category)
	pubDate = models.DateTimeField("Дата публикации", auto_now_add = True)

	def __unicode__(self):
		return self.name

