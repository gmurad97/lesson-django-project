from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "page_name": "Home",
    }
    return render(request, "pages/index.html", context)


def health_and_wellness_category(request):
    context = {
        "page_name": "Health And Wellness Category",
    }
    return render(request, "pages/health_and_wellness_category.html", context)


def gallery_formate(request):
    context = {
        "page_name": "Gallery Formate",
    }
    return render(request, "pages/gallery_formate.html", context)


def full_width_with_sidebar(request):
    context = {
        "page_name": "Full Width With Sidebar",
    }
    return render(request, "pages/full_width_with_sidebar.html", context)


def full_width_with_no_sidebar(request):
    context = {
        "page_name": "Full Width With No Sidebar",
    }
    return render(request, "pages/full_width_with_no_sidebar.html", context)


def faq(request):
    context = {
        "page_name": "Faq",
    }
    return render(request, "pages/faq.html", context)


def editor_profile(request):
    context = {
        "page_name": "Editor Profile",
    }
    return render(request, "pages/editor_profile.html", context)


def contact_us(request):
    context = {
        "page_name": "Contact Us",
    }

    return render(request, "pages/contact_us.html", context)


def classic_with_sidebar(request):
    context = {
        "page_name": "Classic With Sidebar",
    }
    return render(request, "pages/classic_with_sidebar.html", context)


def audio_formate(request):
    context = {
        "page_name": "Audio Formate",
    }
    return render(request, "pages/audio_formate.html", context)


def ai_category(request):
    context = {
        "page_name": "AI Category",
    }
    return render(request, "pages/ai_category.html", context)


def about_us(request):
    context = {
        "page_name": "About Us",
    }
    return render(request, "pages/about_us.html", context)


def video_formate(request):
    context = {
        "page_name": "Video Formate",
    }
    return render(request, "pages/video_formate.html", context)


def vertical_with_sidebar(request):
    context = {
        "page_name": "Vertical With Sidebar",
    }
    return render(request, "pages/vertical_with_sidebar.html", context)


def vertical_with_no_sidebar(request):
    context = {
        "page_name": "Vertical With No Sidebar",
    }
    return render(request, "pages/vertical_with_no_sidebar.html", context)


def travel_category(request):
    context = {
        "page_name": "Travel Category",
    }
    return render(request, "pages/travel_category.html", context)


def terms_condition(request):
    context = {
        "page_name": "Terms Condition",
    }
    return render(request, "pages/terms_condition.html", context)


def standard_formate(request):
    context = {
        "page_name": "Standard Formate",
    }
    return render(request, "pages/standard_formate.html", context)


def privacy_policy(request):
    context = {
        "page_name": "Privacy Policy",
    }
    return render(request, "pages/privacy_policy.html", context)


def post_pagination(request):
    context = {
        "page_name": "Post Pagination",
    }
    return render(request, "pages/post_pagination.html", context)


def podcast_category(request):
    context = {
        "page_name": "Podcast Category",
    }
    return render(request, "pages/podcast_category.html", context)


def pet_category(request):
    context = {
        "page_name": "Pet Category",
    }
    return render(request, "pages/pet_category.html", context)


def only_for_subscriber(request):
    context = {
        "page_name": "Only For Subscriber",
    }
    return render(request, "pages/only_for_subscriber.html", context)


def minimal(request):
    context = {
        "page_name": "Minimal",
    }
    return render(request, "pages/minimal.html", context)


def life_style(request):
    context = {
        "page_name": "Life Style",
    }
    return render(request, "pages/life_style.html", context)


def error_404(request, exception):
    context = {
        "page_name": "Page Not Found",
        "error":True
    }
    return render(request, "pages/error.html", context, status=404)
