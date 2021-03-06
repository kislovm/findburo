from django.contrib import admin
from reccomendation.models import Category,Reccomendation
from sorl.thumbnail.admin import AdminImageMixin


class ReccomendationAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('name', 'pubDate')

admin.site.register(Category)
admin.site.register(Reccomendation, ReccomendationAdmin)