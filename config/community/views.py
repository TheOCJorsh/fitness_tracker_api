from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post, Like, Comment
from .serializers import PostSerializer, CommentSerializer


class PostListCreateView(generics.ListCreateAPIView):

    queryset = Post.objects.all().order_by('-created_at')

    serializer_class = PostSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikePostView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):

        post = Post.objects.get(id=post_id)

        Like.objects.get_or_create(
            user=request.user,
            post=post
        )

        return Response({"message": "Post liked"})


class CommentCreateView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):

        post = Post.objects.get(id=post_id)

        content = request.data.get("content")

        Comment.objects.create(
            user=request.user,
            post=post,
            content=content
        )

        return Response({"message": "Comment added"})