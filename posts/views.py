from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm

class FeedView(LoginRequiredMixin, CreateView, ListView):
    model = Post
    form_class = PostForm
    template_name = 'posts/feed.html'
    context_object_name = 'posts'
    ordering = ['-data_creazione']
    success_url = reverse_lazy('feed')

    # collega in automatico il post a utente che lo scrive
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)