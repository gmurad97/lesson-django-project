""" from django.urls import path
from

u

urlpatterns = [
    path('', views.index, name='blog_index'),  # Маршрут для главной страницы блога
    path('<int:post_id>/', views.detail, name='blog_detail'),  # Маршрут для деталей поста
]
 """

from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("home/", index),
    path("contact/", contact),
    path("faq/", faq),
    path("news/<slug:news_slug>", news_single),
]
