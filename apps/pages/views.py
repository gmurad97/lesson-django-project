from django.shortcuts import render

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


def categories(request):
    context = {
        "page_title": "Categories",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/categories.html", context)


def categories_detail(request, category_slug):
    context = {
        "page_title": "Categories ->",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/categories_detail.html", context)


def about(request):
    context = {
        "page_title": "About",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/about.html", context)


def contact(request):
    context = {
        "page_title": "Contact",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/contact.html", context)


def faq(request):
    context = {
        "page_title": "FAQ",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/faq.html", context)


def privacy(request):
    context = {
        "page_title": "Privacy Policy",
        "partials": {
            "with_slider": True,
            "with_ads": True,
        },
    }

    return render(request, "pages/privacy.html", context)


def terms(request):
    context = {
        "page_title": "Terms & Condition",
        "partials": {
            "with_slider": True,
            "with_ads": True,
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
