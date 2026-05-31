from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def profile_view(request, username):
    user = get_object_or_404(User, username=username)

    profile = user.profile

    context = {
        'profile_user': user,
        'profile': profile,
    }
    return render(request, 'users/profile.html', context)