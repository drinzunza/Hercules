from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Post
from .forms import PostForm
from django.urls import reverse

# Create your views here.


def home(request):
    return render(request, "posts/home.html")

def about(request):
    return render(request, "posts/about.html")

class create(CreateView):
    model = Post
    template_name = "posts/create.html"
    form_class = PostForm
    
    def get_success_url(self) -> str:
        return reverse('feed')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ListPosts(ListView):
    models = Post
    template_name = "posts/feed.html"
    context_object_name = 'posts'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.prefetch_related('reactions').all()