from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework import permissions
from account.permissions import IsOwnerOrReadonly


# class BoardList(APIView):
#     def get(self, request, format=None):
#         boards = Board.objects.filter(status='A')
#         serializer = BoardSerializer(boards, many=True)
#         return Response(serializer.data)
#
#
# class PostList(APIView):
#     def post(self, request, board_id, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(board_id=board_id)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request, board_id, format=None):
#         posts = Post.objects.filter(board_id=board_id, status='A').order_by('-created_at')
#         serializer = PostListSerializer(posts, many=True)
#         return Response(serializer.data)
#
#
# class PostDetail(APIView):
#     def get_object(self, post_id):
#         post = get_object_or_404(Post, pk=post_id)
#         return post
#
#     def get(self, request, post_id, format=None):
#         post = self.get_object(post_id)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def put(self, request, post_id, format=None):
#         post = self.get_object(post_id)
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardViewSet(viewsets.ModelViewSet):
    # permission 추가
    permission_classes = [IsOwnerOrReadonly]
    serializer_class = BoardSerializer
    queryset = Board.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    # permission 추가
    permission_classes = [IsOwnerOrReadonly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
