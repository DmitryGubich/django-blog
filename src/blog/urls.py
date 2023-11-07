from django.urls import path

from blog.views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    about,
    like_post,
    liked_posts,
    tagged,
)

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<slug:slug>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<slug:slug>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("tag/<slug:slug>/", tagged, name="tagged"),
    path("like-post/<slug:slug>/", like_post, name="like-post"),
    path("liked/", liked_posts, name="liked"),
    path("about/", about, name="about"),
]
