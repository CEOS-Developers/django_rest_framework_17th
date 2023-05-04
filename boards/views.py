from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render

from accounts.models import User
from tag.models import Tag
from .forms import CommentForm
from .models import Board, Comment
from django import forms
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Board
from .serializers import BoardSerializer

class BoardList(APIView):
    """
    게시판 생성
    /board/
    """
    def post(self, request, format=None):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    게시판 조회
    /board/
    """
    def get(self, request, format=None):
        queryset = Board.objects.all()
        serializer = BoardSerializer(queryset, many=True)
        return Response(serializer.data)

class BoardDetail(APIView):
    def get_object(self,pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404

    """
    특정 게시판 조회
    /board/{pk}/
    """
    def get(self, request, pk):
        board = self.get_object(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    """
    특정 게시판 수정
    /board/{pk}
    """
    def put(self, request, pk, format=None):
        board = self.get_object(pk)
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    """
    특정 게시판 삭제
    /board/{pk}/
    """
    def delete(self, request, pk, formate=None):
        board = self.get_object(pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def board_write(request):
    return render(request, 'board_write')


def board_detail(request, pk):
    return render(request, 'board_detail.html')


def board_list(request):
    return render(request, 'board_list.html')


def board_write(request):
    if not request.session.get('user'):
        return redirect('/accounts/login')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)
            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            for tag in tags:
                if not tag:
                    continue
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/boards/list')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})

class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        }, max_length=64, label="제목")
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        },widget=forms.Textarea, label = "내용")
    tags = forms.CharField(required=False, label = "태그")

def comment_write(request, board_id):
    comment_write = CommentForm(request.POST)
    user_id = request.session['user']
    user = User.objects.get(pk=user_id)
    if comment_write.is_valid():
        comments = comment_write.save(commit=False)
        comments.post = get_object_or_404(Board, pk=board_id)
        comments.author = user
        comments.save()
    return redirect('board_detail', board_id)

def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    comments = CommentForm()
    comment_view = Comment.objects.filter(post=pk)
    return render(request, 'board_detail.html',{'board':board, 'comments':comments, 'comment_view':comment_view})