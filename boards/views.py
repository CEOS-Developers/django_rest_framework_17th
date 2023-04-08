from django.http import JsonResponse, Http404

from .serializers import *
from rest_framework.views import APIView


class BoardList(APIView):
	def get(self, request, format=None):
		board_list = Board.objects.all()
		serializer = BoardListSerializer(board_list, many=True)
		return JsonResponse(serializer.data, status=200)


class PostList(APIView):
	def get(self, request):
		post_list = Post.objects.all()
		serializer = PostListSerializer(post_list, many=True)
		return JsonResponse(serializer.data, status=200)


class PostDetail(APIView):
	def get_object(self, pk):
		try:
			return Post.objects.get(pk=pk)

		except Post.DoesNotExist:
			raise Http404("존재하지 않는 게시글입니다.")

	def get(self, pk):
		post = self.get_object(pk)
		serializer = PostSerializer(post)
		return JsonResponse(serializer.data, status=200)

