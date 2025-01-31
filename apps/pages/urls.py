from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("privacy-policy/", index, name="privacy_policy"),
    path("terms-condition/", index, name="terms_condition"),
    path("terms-condition/", index, name="faq"),
    path("terms-condition/", index, name="about"),
    path("terms-condition/", index, name="contact"),
    path("terms-condition/", index, name="news"),
]