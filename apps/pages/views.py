from django.http import Http404
from django.shortcuts import render
from .models import Category, Article

# Create your views here.


def index(request):
    context = {
        "page_title": "Home",
        "categories_last": Category.objects.all()[:5],
        "articles": Article.objects.all()[:9],
    }
    return render(request, "pages/index.html", context)


def categories(request):
    context = {
        "page_title": "Categories",
        "categories_last": Category.objects.all()[:5],
        "categories": Category.objects.all(),
        "hide_slider": True,
    }
    return render(request, "pages/categories.html", context)


def category(request, pk):
    try:
        current_category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise Http404()

    context = {
        "page_title": f"Category {current_category.name}",
        "categories_last": Category.objects.all()[:5],
        "current_category": current_category,
        "articles": Article.objects.filter(category__pk=pk),
        "hide_slider": True,
    }

    if context["articles"].exists():
        return render(request, "pages/category_articles.html", context)
    else:
        raise Http404()


def articles(request):
    context = {
        "page_title": "News",
        "categories_last": Category.objects.all()[:5],
        "articles": Article.objects.all(),
    }
    return render(request, "pages/articles.html", context)


def article(request, pk):
    try:
        current_article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404("Article not found") 

    context = {
        "page_title": f"News - {current_article}",
        "categories_last": Category.objects.all()[:5],
        "current_article": current_article,
        "hide_slider": True,
    }

    return render(request, "pages/article.html", context)


# Success
def faq(request):
    context = {
        "page_title": "FAQ",
        "hide_slider": True,
    }
    return render(request, "pages/faq.html", context)


# Success
def about(request):
    context = {
        "page_title": "About",
        "hide_slider": True,
    }
    return render(request, "pages/about.html", context)


# Success
def privacy_policy(request):
    context = {
        "page_title": "Privacy Policy",
        "hide_slider": True,
    }
    return render(request, "pages/privacy_policy.html", context)


# Success
def terms_condition(request):
    context = {
        "page_title": "Terms & Condition",
        "hide_slider": True,
    }
    return render(request, "pages/terms_condition.html", context)


# Success
def contact(request):
    context = {
        "page_title": "Contact",
        "hide_slider": True,
    }
    return render(request, "pages/contact.html", context)


# Success
def error_404(request, exception):
    context = {
        "page_title": "Page Not Found",
        "categories_last": Category.objects.all()[:5],
        "hide_slider": True,
    }
    return render(request, "pages/error_404.html", context, status=404)
