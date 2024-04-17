from django.shortcuts import render
from .models import Data
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    data = Data.objects.all()
    page = Paginator(data , 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page
    }
    return render(request, 'index.html', context)
