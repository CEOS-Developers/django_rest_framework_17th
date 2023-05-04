from rest_framework import serializers
from community.models import *


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    profile_username = serializers.SerializerMethodField()
    profile_profile_img_path = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'profile', 'profile_username', 'profile_profile_img_path', 'parent', 'contents', 'status',
                  'created_at']

    def get_profile_username(self, obj):
        return obj.profile.user.username

    def get_profile_profile_img_path(self, obj):
        return obj.profile.profile_img_path


class PostSerializer(serializers.ModelSerializer):
    profile_username = serializers.SerializerMethodField()
    profile_profile_img_path = serializers.SerializerMethodField()
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'profile', 'profile_username', 'profile_profile_img_path', 'title', 'contents', 'is_anonymous',
                  'is_question', 'status', 'created_at', 'updated_at', 'comment_set']

    def get_profile_username(self, obj):
        return obj.profile.user.username

    def get_profile_profile_img_path(self, obj):
        return obj.profile.profile_img_path


class PostListSerializer(serializers.ModelSerializer):
    profile_username = serializers.SerializerMethodField()
    profile_profile_img_path = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'profile', 'profile_username', 'profile_profile_img_path', 'title', 'contents', 'is_anonymous',
                  'is_question', 'status', 'created_at', 'updated_at']

    def get_profile_username(self, obj):
        return obj.profile.user.username

    def get_profile_profile_img_path(self, obj):
        return obj.profile.profile_img_path


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'


class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = '__all__'
