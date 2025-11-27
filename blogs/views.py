from django.http import Http404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class PostsListView(ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(is_posted=True)


class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.is_posted:
            raise Http404("Object not found")
        return obj


class PostCreateView(CreateView):
    model = Post
    fields = []
    template_name = "post_form.html"
    success_url = reverse_lazy("home")


class PostUpdateView(UpdateView):
    model = Post
    fields = []
    template_name = "post_form.html"
    success_url = reverse_lazy("post")


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("home")
