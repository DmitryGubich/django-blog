from django.urls import path

from blog.views import about, home

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
]
