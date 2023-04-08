from django.http import Http404
from rest_framework.response import Response

from .serializers import *
from rest_framework.views import APIView


class BoardList(APIView):
	def get(self, request, format=None):
		board_list = Board.objects.all()
		serializer = BoardListSerializer(board_list, many=True)
		return Response(serializer.data, status=200)


class PostList(APIView):
	def get(self, request, board_id, format=None):
		post_list = Post.objects.filter(board__id=board_id)
		serializer = PostListSerializer(post_list, many=True)
		return Response(serializer.data, status=200)

	def post(self, request, board_id, format=None):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(board_id=board_id)
			return Response(status=201)
		return Response(serializer.errors, status=400)


class PostDetail(APIView):
	def get_object(self, post_id):
		try:
			return Post.objects.get(id=post_id)
		except Post.DoesNotExist:
			raise Http404("존재하지 않는 게시글입니다.")

	def get(self, request, board_id, post_id, format=None):
		post = self.get_object(post_id)
		serializer = PostSerializer(post)
		return Response(serializer.data, status=200)

	def delete(self, request, board_id, post_id, format=None):
		post = self.get_object(post_id)
		post.delete()
		return Response(status=204)
