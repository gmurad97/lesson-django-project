from django.shortcuts import render
from .models import Category

# Create your views here.

# Success
def index(request):
    context = {
        "page_title": "Home",
        "categories": Category.objects.all(),
    }
    return render(request, "pages/index.html", context)


def categories(request):
    context = {
        "page_title": "",
    }
    return render(request, "pages/.html", context)


def category(request, pk):
    context = {
        "page_title": "",
    }
    return render(request, "pages/.html", context)


def articles(request):
    context = {
        "page_title": "",
    }
    return render(request, "pages/.html", context)


def article(request, pk):
    context = {
        "page_title": "",
    }
    return render(request, "pages/.html", context)


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
        "hide_slider": True,
    }
    return render(request, "pages/error_404.html", context, status=404)
