#coding: utf-8

from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from urlparse import urlparse

class Category(models.Model):
	key = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name
	def reccomendations(self):
		return Reccomendation.objects.filter(category=self).order_by('-pubDate')

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
	def get_domain(self):
		return urlparse(self.link).netloc
	def photo(self):
		return get_thumbnail(self.image, '600', quality=99)

	category = models.ManyToManyField(Category)
	pubDate = models.DateTimeField("Дата публикации", auto_now_add = True)

	def template(self):
		return {
				"name" : self.name,
				"photo" : self.photo(),
				"about" : self.about,
				"appstore" : self.appstore,
				"google" : self.google,
				"youtube" : self.youtube,
				"facebook" : self.facebook,
				"vk" : self.vk,
				"link" : self.link,
				"get_domain" : self.get_domain,
			}

	def __unicode__(self):
		return self.name

