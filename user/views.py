from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from user.forms import SignupForm


def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account was successfully created.")
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})


@login_required
def profile(request):
    context = {"title": "My profile"}
    return render(request, "profile.html", context)
