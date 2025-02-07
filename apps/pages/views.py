from django.db.models import Count
from django.shortcuts import render
from .models import Category, Article, Slider, Faq, Contact,Setting

# Create your views here.


def index(request):
    context = {
        "page_title": "Home",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }
    return render(request, "pages/index.html", context)


def news(request):
    context = {
        "page_title": "News",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/news.html", context)


def news_detail(request, article_slug):
    context = {
        "page_title": "News -> ",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/news_detail.html", context)


# PREPARE
def categories(request):

    categories = (
        Category.objects.filter(status=True)
        .annotate(article_count=Count("articles"))
        .filter(article_count__gt=0)
        .order_by("-created_at")
    )

    categories_menu = categories[:6]

    settings = Setting.objects.first()

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
        "settings":settings
    }

    return render(request, "pages/categories.html", context)


def category_articles(request, category_slug):
    context = {
        "page_title": "Categories ->",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/category_articles.html", context)


def about(request):
    context = {
        "page_title": "About",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
    }

    return render(request, "pages/about.html", context)


def contact(request):
    context = {
        "page_title": "Contact",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
    }

    return render(request, "pages/contact.html", context)


def faq(request):
    context = {
        "page_title": "FAQ",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
    }

    return render(request, "pages/faq.html", context)


def privacy(request):
    context = {
        "page_title": "Privacy Policy",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
    }

    return render(request, "pages/privacy.html", context)


def terms(request):
    context = {
        "page_title": "Terms & Condition",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
    }

    return render(request, "pages/terms.html", context)


def error_404(request, exception):
    context = {
        "page_title": "Page Not Found",
        "partials": {
            "with_slider": False,
            "with_ads": False,
        },
    }

    return render(request, "pages/errors/error_404.html", context, status=404)
