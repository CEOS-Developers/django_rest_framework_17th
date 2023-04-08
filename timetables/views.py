from django.http import Http404
from rest_framework.response import Response

from .serializers import *
from rest_framework.views import APIView


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
        print(friends_serializer.data)
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
            serializer.save()
            return Response(status=201)
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









