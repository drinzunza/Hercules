from django.urls import path
from .views import home, about, create, ListPosts, add_reaction


urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('posts/create', create.as_view(), name="create_post"),
    path('posts/feed', ListPosts.as_view(), name="feed"),
    path('post/react/<int:post_id>', add_reaction, name="react"),
]
