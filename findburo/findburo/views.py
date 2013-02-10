from reccomendation.models import Reccomendation,Category
from django.shortcuts import render_to_response

def index(request):
    category_list = Category.objects.all()
    reccomendation_list = Reccomendation.objects.filter(category=category_list[:1])
    return render_to_response('index.html', { "category_list": category_list,
    	"reccomendation_list": reccomendation_list })
