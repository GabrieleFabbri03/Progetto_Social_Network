from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    context = {
        'profile_user': user,
        'profile': profile,
    }
    return render(request, 'users/profile.html', context)


def register(request):
    # Se l'utente ha premuto "Invia" sul form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Salva il nuovo utente nel database
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    mio_profilo = request.user.profile

    if request.user != user_to_follow:
        if user_to_follow.profile in mio_profilo.follows.all():
            mio_profilo.follows.remove(user_to_follow.profile)
        else:
            mio_profilo.follows.add(user_to_follow.profile)

    return HttpResponseRedirect(reverse('profile', args=[username]))