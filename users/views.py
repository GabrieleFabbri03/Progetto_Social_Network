from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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