from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView
from .models import Profile

def profile_view(request, username):
    # Utente da visualizzare
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)

    if request.user.is_authenticated:
        Profile.objects.get_or_create(user=request.user)

    context = {
        'profile_user': user,
        'profile': profile,
    }
    return render(request, 'users/profile.html', context)


@login_required
def ban_user(request, username):
    if not request.user.is_staff:
        return redirect('feed')

    user_to_ban = get_object_or_404(User, username=username)

    # Un Mod non può bannare un Admin (superuser)
    if user_to_ban.is_superuser and not request.user.is_superuser:
        return redirect('profile', username=username)

    if request.user != user_to_ban:
        if request.method == 'POST':
            user_to_ban.is_active = not user_to_ban.is_active
            user_to_ban.save()

    return redirect('profile', username=username)


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

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['bio']
    template_name = 'users/profile_edit.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.request.user.username})