from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name="konoha"),
    path('news', views.news, name="news"),

]
