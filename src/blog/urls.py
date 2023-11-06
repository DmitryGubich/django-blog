from django.urls import path

from blog.views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    about,
)

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<slug:slug>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<slug:slug>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("about/", about, name="about"),
]
