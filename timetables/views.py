import logging

from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, filters
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


# class TimetableViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['user_id']

#
#
# class CourseFilter(FilterSet):
#     title = filters.CharFilter(method='filter_is_title')
#     professor = filters.CharFilter(field_name='professor')
#
#     class Meta:
#         model = CourseDetail
#         fields = ['title', 'professor']
#
#     def filter_is_title(self, queryset, name, value):
#         return queryset.filter(title=value)


# class CourseViewSet(viewsets.ModelViewSet):
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'professor']


# log 사용
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TimetableDetail(APIView):
    def get_object(self, timetable_id):
        try:
            return Timetable.objects.get(id=timetable_id)
        except Timetable.DoesNotExist:
            raise Http404("존재하지 않는 시간표입니다.")

    def get(self, request, timetable_id, format=None):
        timetable = Timetable.objects.get(id=timetable_id)
        timetable_serializer = TimetableSerializer(timetable)
        friends = Friend.objects.filter(from_user__id=timetable.user.id)
        friends_serializer = FriendSerializer(friends, many=True)
        serializers = [timetable_serializer.data, friends_serializer.data]
        return Response(serializers, status=200)

    def delete(self, request, timetable_id, format=None):
        timetable = self.get_object(timetable_id)
        timetable.delete()
        return Response(status=204)


class TimetableList(APIView):
    def get(self, request, format=None):
        timetable_list = Timetable.objects.filter(user__nickname=request.data.get('nickname'))
        serializer = TimetableListSerializer(timetable_list, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = TimetableSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(nickname=request.data.get('nickname'))
            serializer.save(user=user)
            return self.get(request)
        return Response(serializer.errors, status=400)


class CourseDetailView(APIView):
    def get(self, request, format=None):
        # 강의명과 교수명으로 검색할 수 있다고 가정하였다
        if request.data.get('title') is not None:
            course_list = CourseDetail.objects.filter(course__title__contains=request.data.get('title'))
        else:
            course_list = CourseDetail.objects.filter(course__professor__contains=request.data.get('professor'))
        serializer = CourseDetailSerializer(course_list, many=True)
        return Response(serializer.data, status=200)
