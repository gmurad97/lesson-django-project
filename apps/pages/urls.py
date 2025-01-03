from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("about-us/", about_us, name="about_us"),
    path("audio-formate/", audio_formate, name="audio_formate"),
    path("classic-with-siderbar/", classic_with_siderbar, name="classic_with_siderbar"),
    path("contact-us/", contact_us, name="contact_us"),
    path("editor-profile/", editor_profile, name="editor_profile"),
    path("faq/", faq, name="faq"),
    path("full-widht-with-no-sidebar/", full_widht_with_no_sidebar, name="full_widht_with_no_sidebar"),
    path("full-widht-with-sideber/", full_widht_with_sideber, name="full_widht_with_sideber"),
    path("gallery-formate/", gallery_formate, name="gallery_formate"),
    path("health-and-wellness-category/", health_and_wellness_category, name="health_and_wellness_category"),
    path("only-for-subscriber/", only_for_subscriber, name="only_for_subscriber"),
    path("post-pagination/", post_pagination, name="post_pagination"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
    path("standard-formate/", standard_formate, name="standard_formate"),
    path("terms-condition/", terms_condition, name="terms_condition"),
    path("vertical-with-no-sidebar/", vertical_with_no_sidebar, name="vertical_with_no_sidebar"),
    path("vertical-with-sidebar/", vertical_with_sidebar, name="vertical_with_sidebar"),
    path("video-formate/", video_formate, name="video_formate"),
]
