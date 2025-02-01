from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("categories/", categories, name="categories"),
    path("category/<int:pk>/", category, name="category"),
    path("articles/", articles, name="articles"),
    path("article/<int:pk>/", article, name="article"),
    path("faq/", faq, name="faq"),
    path("about/", about, name="about"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
    path("terms-condition/", terms_condition, name="terms_condition"),
    path("contact/", contact, name="contact"),
]
