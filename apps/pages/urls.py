from django.urls import path
from .views import *

app_name = "pages"

urlpatterns = [
    path("", index, name="home"),
    path("news/", news, name="news_list"),
    path("news/<slug:article_slug>", news_detail, name="news_detail"),
    path("categories/", categories, name="categories_list"),
    path("categories/<slug:category_slug>", categories_detail, name="category_detail"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("faq/", faq, name="faq"),
    path("privacy/", privacy, name="privacy"),
    path("terms/", terms, name="terms"),
]
