from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets
from rest_framework import mixins
import django_filters
# Create your views here.
#filterset
class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = ['title', 'created_at', 'updated_at']
        order_by = ['update_at']

# viewset
class PostViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
class CommentList(APIView) :
    """
    댓글 생성
    /comment/
    """
    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    댓글 조회
    /comment/
    """
    #def get(self,request, format=None):
    #    queryset = Comment.objects.all()
    #    serializer = CommentSerializer(queryset, many=True)
    #    return Response(serializer.data)

class CommentDetail(APIView) :
    def get_object(self,pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist :
            raise Http404

    """
    특정 댓글 조회
    /comment/{pk}/
    """
    def get(self, request, pk):
        comments = self.get_object(pk)
        serializer = CommentSerializer(comments)
        return Response(serializer.data)

    """
    특정 댓글 수정
    /comment/{pk}/
    """
    def put(self, request, pk, format=None):
        comments = self.get_object(pk)
        serializer = CommentSerializer(comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    특정 댓글 삭제
    /comment/{pk}/
    """
    def delete(self,request,pk,format=None):
        comments = self.get_object(pk)
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#class Login(APIView):

 #   def post(self, request):
 #       user = authenticate(username=request.data.get("username"), password=request.data.get("password"))

        #if user is not None:
        #    token = TokenObtainPairSerializer.get_token(user)
        #    access_token = token.access_token
        #    res = Response(
        #        {
        #            "message": "login success",
        #            "token": str(token.access_token)
        #        },
        #        status=status.HTTP_200_OK,
        #    )

         #   res.set_cookie("access", access_token, httponly=True)
         #   return res
        #else:
        #    return HttpResponse("target failed")