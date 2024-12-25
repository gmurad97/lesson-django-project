from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {"title": "Home"}
    return render(request, "pages/index.html", context)


def category(request):
    context = {"title": "Category"}
    return render(request, "pages/health-and-wellness-category.html", context)


def news_single(request):
    context = {"title": "News Full With Sidebar"}
    return render(request, "pages/full-widht-with-sideber.html", context)


def faq(request):
    context = {"title": "FAQ"}
    return render(request, "pages/faq.html", context)


def contact(request):
    context = {"title": "Contact Us"}
    return render(request, "pages/contact-us.html", context)


def about(request):
    context = {"title": "About Us"}
    return render(request, "pages/about-us.html", context)


def privacy_policy(request):
    context = {"title": "Privacy Policy"}
    return render(request, "pages/privacy-policy.html", context)


def news(request):
    context = {"title": "News Standart Formate"}
    return render(request, "pages/standard-formate.html", context)


def terms_and_condition(request):
    context = {"title": "Terms & Condition"}
    return render(request, "pages/terms-and-condition.html", context)


def handle_404(request, exception):
    context = {"title": "Page Not Found"}
    return render(request, "pages/error.html", context, status=404)
