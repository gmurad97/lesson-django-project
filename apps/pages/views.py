from django.http import Http404
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *

# Create your views here.


def index(request):
    advertising = Advertising.objects.first()
    sliders = Slider.objects.filter(status=True)
    categories = (
        Category.objects.filter(status=True)
        .annotate(article_count=Count("articles"))
        .filter(article_count__gt=0)
        .order_by("-created_at")
    )
    categories_last = categories[:7]
    articles = Article.objects.filter(status=True)
    articles_last = articles[:3]
    settings = Setting.objects.first()

    context = {
        "page_title": "Home",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
        "sliders": sliders,
        "ads": advertising,
        "categories": {
            "all": categories,
            "last": categories_last,
        },
        "articles": {
            "all": articles,
            "last": articles_last,
        },
        "settings": settings,
    }

    return render(request, "pages/index.html", context)


# rotter
def home(request):
    return redirect(reverse("pages:home"))


# rotter
def news(request):
    context = {
        "page_title": "News",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/news.html", context)


# rotter
def news_detail(request, article_slug):
    context = {
        "page_title": "News -> ",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/news_detail.html", context)


# rotter
def categories(request):

    categories = (
        Category.objects.filter(status=True)
        .annotate(article_count=Count("articles"))
        .filter(article_count__gt=0)
        .order_by("-created_at")
    )

    categories_menu = categories[:6]

    settings = Setting.objects.first()

    advertising = Advertising.objects.first()

    context = {
        "page_title": "Categories",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
        "categories": {
            "all": categories,
            "menu": categories_menu,
        },
        "settings": settings,
        "ads": advertising,
    }

    return render(request, "pages/categories.html", context)


# rotter
def category_articles(request, category_slug):
    context = {
        "page_title": "Categories ->",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/category_articles.html", context)


# rotter
def about(request):
    context = {
        "page_title": "About",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
    }

    return render(request, "pages/about.html", context)


# rotter
def contact(request):
    context = {
        "page_title": "Contact",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
    }

    return render(request, "pages/contact.html", context)


# rotter
def faq(request):
    faqs = Faq.objects.filter(status=True)  # tolko tut

    context = {
        "page_title": "FAQ",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
        "faqs": faqs,
    }

    return render(request, "pages/faq.html", context)


# rotter
def privacy(request):
    context = {
        "page_title": "Privacy Policy",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
    }

    return render(request, "pages/privacy.html", context)


# rotter
def terms(request):
    context = {
        "page_title": "Terms & Condition",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
    }

    return render(request, "pages/terms.html", context)


# rotter
def error_404(request, exception):
    context = {
        "page_title": "Page Not Found",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
    }

    return render(request, "pages/errors/error_404.html", context, status=404)
