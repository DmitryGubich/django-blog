from django.shortcuts import render

posts = [
    {
        "author": "Admin",
        "title": "First post",
        "content": "Content of the first post",
        "date_posted": "3 Nov, 2023",
    },
    {
        "author": "User",
        "title": "Second post",
        "content": "Content of the second post",
        "date_posted": "23 Sep, 2023",
    },
]


def home(request):
    context = {"title": "Main", "posts": posts}
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html", {"title": "About"})
