from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from user.forms import SignupForm, UserUpdateForm


def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was successfully created.")
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "user/signup.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was successfully updated.")
            return redirect("profile")

    else:
        form = UserUpdateForm(instance=request.user)

    context = {"form": form}

    return render(request, "user/profile.html", context)
