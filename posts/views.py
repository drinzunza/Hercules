from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import Post, PostReactions 
from .forms import PostForm
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, "posts/home.html")

def about(request):
    return render(request, "posts/about.html")

def add_reaction(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    reaction_type = request.POST.get('reaction')
    
    record, created = PostReactions.objects.get_or_create(post=post, user=user)
    record.like = False
    record.dislike = False
    record.heart = False
    
    if reaction_type == 'like':
        record.like = True
    elif reaction_type == 'dislike':
        record.dislike = True
    else:
        record.heart = True
        
    record.save()
    
    response = {
        'likes': post.reactions.filter(like=True).count(),
        'dislikes': post.reactions.filter(dislike=True).count(),
        'heart': post.reactions.filter(heart=True).count(),
        
    }
    
    return JsonResponse(response)

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = context['posts']
        for post in posts:
            post.like_count = PostReactions.objects.filter(post=post, like=True).count()
            post.dislike_count = PostReactions.objects.filter(post=post, dislike=True).count()
            post.heart_count = PostReactions.objects.filter(post=post, heart=True).count()
        return context