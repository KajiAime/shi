from rest_framework import generics
from .models import User, Post, Comments, Follow, Notification, Messages, Post_like, Post_type, Hashtags
from .serializers import UserSerializer, PostSerializer, CommentSerializer, FollowSerializer, NotificationSerializer, MessageSerializer, Post_likeSerializer, Post_typeSerializer, HashtagSerializer
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class FollowList(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

class FollowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

class NotificationList(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class MessageList(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer

class Post_likeList(generics.ListCreateAPIView):
    queryset = Post_like.objects.all()
    serializer_class = Post_likeSerializer

class Post_likeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_like.objects.all()
    serializer_class = Post_likeSerializer

class Post_typeList(generics.ListCreateAPIView):
    queryset = Post_type.objects.all()
    serializer_class = Post_typeSerializer

class Post_typeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_type.objects.all()
    serializer_class = Post_typeSerializer

class HashtagsList(generics.ListCreateAPIView):
    queryset = Hashtags.objects.all()
    serializer_class = HashtagSerializer

class TodoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hashtags.objects.all()
    serializer_class = HashtagSerializer