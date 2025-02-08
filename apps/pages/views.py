from django.db.models import Count
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *


def get_common_context():
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
    articles_home = articles[:9]
    articles_last = articles[:3]
    settings = Setting.objects.first()

    return {
        "sliders": sliders,
        "ads": advertising,
        "categories": {
            "all": categories,
            "last": categories_last,
        },
        "articles": {
            "all": articles,
            "home": articles_home,
            "last": articles_last,
        },
        "settings": settings,
    }


# Create your views here.


def index(request):
    context = get_common_context()
    context.update(
        {
            "page_title": "Home",
            "partials": {
                "with_slider": True,
                "with_ads": True,
            },
        }
    )
    return render(request, "pages/index.html", context)


def home(request):
    return redirect(reverse("pages:home"))


def news(request):
    context = get_common_context()
    context.update(
        {
            "page_title": "News",
            "partials": {
                "with_slider": True,
                "with_ads": True,
            },
        }
    )
    return render(request, "pages/articles.html", context)


def news_detail(request, article_slug):
    context = get_common_context()
    context.update(
        {
            "page_title": "News -> ",
            "partials": {
                "with_slider": True,
                "with_ads": True,
            },
        }
    )
    return render(request, "pages/article_detail.html", context)


def categories(request):
    context = get_common_context()
    context.update(
        {
            "page_title": "Categories",
            "partials": {
                "with_slider": False,
                "with_ads": False,
            },
        }
    )
    return render(request, "pages/categories.html", context)


def category_articles(request, category_slug):
    category_instance = Category.objects.filter(slug=category_slug, status=True).first()
    if not category_instance:
        raise Http404("Category not found")

    category_articles = Article.objects.filter(category=category_instance, status=True)
    context = get_common_context()
    context.update(
        {
            "page_title": f"Category: {category_instance.name}",
            "partials": {
                "with_slider": True,
                "with_ads": True,
            },
            "category_instance": category_instance,
            "category_articles": category_articles,
        }
    )

    return render(request, "pages/category_articles.html", context)


def about(request):
    context = get_common_context()
    context.update(
        {
            "page_title": "About",
            "partials": {
                "with_slider": False,
                "with_ads": False,
            },
        }
    )
    return render(request, "pages/about.html", context)


def contact(request):
    context = get_common_context()
    context.update(
        {
            "page_title": "Contact",
            "partials": {
                "with_slider": False,
                "with_ads": False,
            },
        }
    )
    return render(request, "pages/contact.html", context)


def faq(request):
    faqs = Faq.objects.filter(status=True)
    context = get_common_context()
    context.update(
        {
            "page_title": "FAQ",
            "partials": {
                "with_slider": False,
                "with_ads": False,
            },
            "faqs": faqs,
        }
    )
    return render(request, "pages/faq.html", context)


def privacy(request):
    context = get_common_context()
    context.update(
        {
            "page_title": "Privacy Policy",
            "partials": {
                "with_slider": False,
                "with_ads": False,
            },
        }
    )
    return render(request, "pages/privacy.html", context)


def terms(request):
    context = get_common_context()
    context.update(
        {
            "page_title": "Terms & Condition",
            "partials": {
                "with_slider": False,
                "with_ads": False,
            },
        }
    )
    return render(request, "pages/terms.html", context)


def error_404(request, exception):
    context = get_common_context()
    context.update(
        {
            "page_title": "Page Not Found",
            "partials": {
                "with_slider": False,
                "with_ads": False,
            },
        }
    )
    return render(request, "pages/errors/error_404.html", context, status=404)
