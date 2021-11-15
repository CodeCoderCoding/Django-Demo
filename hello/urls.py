# hello/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<path:title>/', views.article_title),
    path('articles/search_form/', views.search_form),
    path('articles/search/', views.search),
    path('articles/search_post/', views.search_post)
]

