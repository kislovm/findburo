#coding: utf-8

from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from urlparse import urlparse
import random

class Category(models.Model):
	key = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name
	def reccomendations(self):
		return Reccomendation.objects.filter(category=self).order_by('-weight','-pubDate')

class Reccomendation(models.Model):
	name = models.CharField("Заголовок",max_length=200)
	image = ImageField(upload_to='reccomendation', null=True)
	about = models.TextField("Описание", blank=True)
	appstore = models.URLField("Аппстор", blank=True)
	google = models.URLField("Гугл Плэй", blank=True)
	youtube = models.URLField("Ютуб", blank=True)
	facebook = models.URLField("Facebook", blank=True)
	vk = models.URLField("Вконтакте", blank=True)
	link = models.URLField("Ссылка", blank=True)
	weight = models.IntegerField("Вес", default=10)
	def get_domain(self):
		return urlparse(self.link).netloc
	def photo(self):
		return get_thumbnail(self.image, '600', quality=99)

	category = models.ManyToManyField(Category)
	pubDate = models.DateTimeField("Дата публикации", auto_now_add = True)
	def commentsCount(self):
		random.seed(self.name)
		return random.randrange(5,20)	

	def template(self):
		return {
				"name" : self.name,
				"photo" : { "url" : self.photo().url },
				"about" : self.about,
				"appstore" : self.appstore,
				"google" : self.google,
				"youtube" : self.youtube,
				"facebook" : self.facebook,
				"vk" : self.vk,
				"link" : self.link,
				"get_domain" : self.get_domain(),
				"commentsCount" : self.commentsCount(),
			}

	def __unicode__(self):
		return self.name

