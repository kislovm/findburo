import json
from django.core import serializers
from models import Category
from django.http import HttpResponse

def category_reccomendations(request, key):
	json_serializer = serializers.get_serializer("json")()
	category = Category.objects.filter(key=key)[0]
	response = [ x.template() for x in category.reccomendations() ]
	return HttpResponse(response)