from django.contrib import admin
from reccomendation.models import Category,Reccomendation

class ReccomendationAdmin(admin.ModelAdmin):
	list_display = ('name', 'pubDate')

admin.site.register(Category)
admin.site.register(Reccomendation, ReccomendationAdmin)