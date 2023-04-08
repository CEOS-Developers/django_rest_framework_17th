from rest_framework import serializers
from boards.models import *


class CommentReplySerializer(serializers.ModelSerializer):
    user_nickname = serializers.SerializerMethodField()

    class Meta:
        model = CommentReply
        fields = ['user', 'user_nickname', 'content', 'like_number', 'created_at']

    def get_user_nickname(self, obj):
        return obj.user.nickname


class CommentSerializer(serializers.ModelSerializer):
    user_nickname = serializers.SerializerMethodField()
    comment_replies = CommentReplySerializer(many=True)

    class Meta:
        model = Comment
        fields = ['user', 'user_nickname', 'content', 'like_number', 'comment_replies', 'created_at']

    def get_user_nickname(self, obj):
        return obj.user.nickname


class PostSerializer(serializers.ModelSerializer):
    user_nickname = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['user', 'user_nickname', 'title', 'content', 'like_number', 'comments_count', 'created_at', 'comments']

    def get_user_nickname(self, obj):
        return obj.user.nickname

    def get_comments_count(self, obj):
        reply_count = 0

        for comment in obj.comments.all():
            reply_count += comment.comment_replies.count()

        return obj.comments.count() + reply_count


class PostListSerializer(serializers.ModelSerializer):
    user_nickname = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['user', 'user_nickname', 'title', 'content', 'like_number', 'comments_count', 'created_at']


    def get_user_nickname(self, obj):
        return obj.user.nickname

    def get_comments_count(self, obj):
        reply_count = 0

        for comment in obj.comments.all():
            reply_count += comment.comment_replies.count()

        return obj.comments.count() + reply_count

    # 시간 돌려주는 함수를 짰으면 좋겠땅...


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['name', 'description']





