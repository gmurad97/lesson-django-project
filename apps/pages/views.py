from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title": "Home & Index Page",
    }
    return render(request, "pages/index.html", context)


def about_us(request):
    context = {
        "title": "About Page",
    }
    return render(request, "pages/about-us.html", context)


def audio_formate(request):
    context = {
        "title": "Audio Formate Page",
    }
    return render(request, "pages/audio-formate.html", context)


def classic_with_siderbar(request):
    context = {
        "title": "Classic With Sidebar Page",
    }
    return render(request, "pages/classic-with-sidebar.html", context)


def contact_us(request):
    context = {
        "title": "Contact Us Page",
    }
    return render(request, "pages/contact-us.html", context)


def editor_profile(request):
    context = {
        "title": "Editor Profile Page",
    }
    return render(request, "pages/editor-profile.html", context)


def faq(request):
    context = {
        "title": "FAQ Page",
    }
    return render(request, "pages/faq.html", context)


def full_widht_with_no_sidebar(request):
    context = {
        "title": "Full Widht With No Sidebar Page",
    }
    return render(request, "pages/full-widht-with-no-sidebar.html", context)


def full_widht_with_sideber(request):
    context = {
        "title": "Full Widht With Sideber Page",
    }
    return render(request, "pages/full-widht-with-sideber.html", context)


def gallery_formate(request):
    context = {
        "title": "Gallery Formate Page",
    }
    return render(request, "pages/gallery-formate.html", context)


def health_and_wellness_category(request):
    context = {
        "title": "Health And Wellness Category Page",
    }
    return render(request, "pages/health-and-wellness-category.html", context)


def only_for_subscriber(request):
    context = {
        "title": "Only For Subscriber Page",
    }
    return render(request, "pages/only-for-subscriber.html", context)


def post_pagination(request):
    context = {
        "title": "Post Pagination Page",
    }
    return render(request, "pages/post-pagination.html", context)


def privacy_policy(request):
    context = {
        "title": "Privacy Policy Page",
    }
    return render(request, "pages/privacy-policy.html", context)


def standard_formate(request):
    context = {"title": "Standard Formate Page"}
    return render(request, "pages/standard-formate.html", context)


def terms_condition(request):
    context = {
        "title": "Terms Condition Page",
    }
    return render(request, "pages/terms-condition.html", context)


def vertical_with_no_sidebar(request):
    context = {
        "title": "Vertical With No Sidebar Page",
    }
    return render(request, "pages/vertical-with-no-sidebar.html", context)


def vertical_with_sidebar(request):
    context = {
        "title": "Vertical With Sidebar Page",
    }
    return render(request, "pages/vertical-with-sidebar.html", context)


def video_formate(request):
    context = {
        "title": "Video Formate Page",
    }
    return render(request, "pages/video-formate.html", context)


def error_404(request, exception):
    context = {
        "title": "Video Formate Page",
        "is_404": True,
    }
    return render(request, "pages/error.html", context, status=404)
