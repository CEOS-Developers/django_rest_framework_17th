from rest_framework import serializers
from .models import *
from global_entity.models import *
from account.models import *


class BoardSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    university = University()

    class Meta:
        model = Board  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함


class PostSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    board = Board()
    writer = User()

    class Meta:
        model = Post  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함


class FriendshipSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =

    from_user = User()
    to_user = User()

    class Meta:
        model = Friendship  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함


class CommentSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    comment = Comment()
    writer = User()

    class Meta:
        model = Comment  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함


class LikePostSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    post = Post()
    who = User()

    class Meta:
        model = LikePost  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함


class ScrapPostSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    post = Post()
    who = User()

    class Meta:
        model = ScrapPost  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함


class BlackPostSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    post = Post()
    who = User()

    class Meta:
        model = BlackPost  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함


class LikeCommentSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    comment = Comment()
    who = User()

    class Meta:
        model = LikeComment  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함


class BlackCommentSerializer(serializers.ModelSerializer):
    # __all__ 이라가하면 필드 명시할 필요가 없음
    # university =
    comment = Comment()
    who = User()

    class Meta:
        model = BlackComment  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함
