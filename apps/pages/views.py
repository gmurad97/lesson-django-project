from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title": "Home"
    }
    return render(request, "pages/index.html",context)


def contact(request):
    context = {
        "title": "Contact Page"
    }
    return render(request, "pages/contact-us.html",context)


def faq(request):
    context = {
        "title": "Faq"
    }
    return render(request, "pages/faq.html",context)


def news_single(request,news_slug):
    context = {
        "title": f"News {news_slug}"
    }
    return render(request, "pages/standard-formate.html",context)


def error_404(request, exception):
    context = {
        "title": "News"
    }
    return render(request, "pages/error.html",context)
