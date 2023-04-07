from rest_framework import serializers
from account.serializers import UserSerializer
from .models import *


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer
    board = BoardSerializer

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer
    post = PostSerializer

    class Meta:
        model = Comment
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    user = UserSerializer
    comment = CommentSerializer

    class Meta:
        model = Reply
        fields = '__all__'
