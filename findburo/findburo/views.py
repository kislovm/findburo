from reccomendation.models import Reccomendation,Category
from django.shortcuts import render_to_response

def index(request, category = False):
    category_list = Category.objects.all()
    if category:
        selected = category_list.filter(key=category)
    else:
        selected = category_list
    reccomendation_list = selected[0].reccomendations()
    return render_to_response('index.html', { "category_list": category_list,
    	"reccomendation_list": reccomendation_list, "selected": selected[0] })
