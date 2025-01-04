from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("about-us/", about_us, name="about-us"),
    path("audio-formate/", audio_formate, name="audio-formate"),
    path("classic-with-siderbar/", classic_with_siderbar, name="classic-with-siderbar"),
    path("contact-us/", contact_us, name="contact-us"),
    path("editor-profile/", editor_profile, name="editor-profile"),
    path("faq/", faq, name="faq"),
    path("full-widht-with-no-sidebar/", full_widht_with_no_sidebar, name="full-widht-with-no-sidebar"),
    path("full-widht-with-sideber/", full_widht_with_sideber, name="full-widht-with-sideber"),
    path("gallery-formate/", gallery_formate, name="gallery-formate"),
    path("health-and-wellness-category/", health_and_wellness_category, name="health-and-wellness-category"),
    path("only-for-subscriber/", only_for_subscriber, name="only-for-subscriber"),
    path("post-pagination/", post_pagination, name="post-pagination"),
    path("privacy-policy/", privacy_policy, name="privacy-policy"),
    path("standard-formate/", standard_formate, name="standard-formate"),
    path("terms-condition/", terms_condition, name="terms-condition"),
    path("vertical-with-no-sidebar/", vertical_with_no_sidebar, name="vertical-with-no-sidebar"),
    path("vertical-with-sidebar/", vertical_with_sidebar, name="vertical-with-sidebar"),
    path("video-formate/", video_formate, name="video-formate"),
]
