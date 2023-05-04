from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Board, Post, Friendship, Comment, LikePost
from .serializers import *
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from rest_framework import viewsets

from django_filters.rest_framework import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
#
# class AllBoardView(APIView):
#     def get(self, request, format=None):  # 모든 게시판
#         try:
#             board_lists = Board.objects.all()
#             serializer = BoardSerializer(board_lists, many=True)
#             # 리스트로 반환하는 boardlists
#             return Response(serializer.data)
#         except AttributeError as e:
#             # print(e)
#             return Response("message: error")
#
#     def post(self, request, format=None):
#         data = request.data
#         serializer = BoardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# class OneBoardView(APIView):
#     def get(self, request, pk):  # 원하는 게시판 가져오기
#         try:
#             board = Board.objects.get(board_id=pk)
#             serializer = BoardSerializer(board)
#             return Response(serializer.data, status=201)
#         except ObjectDoesNotExist as e:
#             # print(e)
#             return Response({"message: error"})
#
#     def delete(self, request, pk):
#         # soft delete #post(deleted_at 넣어주면 되니까?)
#         try:
#             board = Board.objects.get(board_id=pk)
#             # I want to change the value of is_deleted to True
#             board.is_deleted = True
#             board.save()
#             return Response(status=200)
#         except ObjectDoesNotExist as e:
#             # print(e)
#             return Response({"message: not exist"})
#

# filter
from rest_framework import viewsets
from .serializers import *
from django_filters.rest_framework import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend


class BoardFilter(FilterSet):
    # 필터 걸 속성
    name = filters.CharFilter(field_name='name')
    university_id = filters.NumberFilter(field_name='university_id_id')

    class Meta:
        model = Board  # 사용할 모델
        fields = ['name', 'university_id']  # 사용할 속성


# ModelViewSet을 상속함으로써 crud 기능이 5줄로 끝남
class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = BoardFilter

    # perform destory 를 override 해서 soft delete 구현
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
