from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm
class FeedView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/feed.html'
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Forza l'ordine decrescente
        context['posts'] = Post.objects.all().order_by('-data_creazione')
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('feed')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('feed')

    def test_func(self):
        post = self.get_object()

        #Se sei l'autore del post puoi sempre cancellarlo
        if self.request.user == post.author:
            return True
        #Se sei admin puoi cancellare tutto
        if self.request.user.is_superuser:
            return True
        #Se è mod puoi cancellare ma non i post dell'admin
        if self.request.user.is_staff and not post.author.is_superuser:
            return True

        return False