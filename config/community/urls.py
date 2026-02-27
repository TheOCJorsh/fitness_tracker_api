from django.urls import path
from .views import PostListCreateView, LikePostView, CommentCreateView

urlpatterns = [

    path('posts/', PostListCreateView.as_view()),

    path('posts/<int:post_id>/like/', LikePostView.as_view()),

    path('posts/<int:post_id>/comment/', CommentCreateView.as_view()),

]