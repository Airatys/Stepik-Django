from contextlib import redirect_stderr

from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    t = render_to_string('women/index.html')
    return HttpResponse(t)

def about(request):
    return render(request, 'women/about.html')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p >id:{cat_id}</p>')

def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p >:{cat_slug}</p>')

def archive(request, year):
    if year > 2023:
        url_redirect = reverse('cats', args=('music', ))
        return redirect(url_redirect, permanent=True) #HttpResponsePermanentRedirect('home', permanent=True)
        # raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')