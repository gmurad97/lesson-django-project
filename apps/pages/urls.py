from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="home"),
    path("category/", category, name="category"),
    path("faq/", faq, name="faq"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("terms/", terms_and_condition, name="terms"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
    path("news-standart/", news, name="news_standart"),
    path("news-default/", news_single, name="news_default"),
]
