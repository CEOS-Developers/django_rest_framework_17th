from django.http import Http404
from rest_framework.response import Response

from .serializers import *
from rest_framework.views import APIView


class Timetable(APIView):
    def get_object(self, timetable_id):
        try:
            return Timetable.objects.get(id=timetable_id)
        except Timetable.DoesNotExist:
            raise Http404("존재하지 않는 시간표입니다.")

    def get(self, request, timetable_id, format=None):
        timetable = Timetable.objects.get(id=timetable_id)
        timetable_serializer = TimetableSerializer(timetable)
        friends = Friend.objects.get(from_user=request.GET['nickname'])
        friends_serializer = FriendSerializer(friends, many=True)
        return Response(timetable_serializer.data, friends_serializer, status=200)

    def delete(self, request, timetable_id, format=None):
        timetable = self.get_object(timetable_id)
        timetable.delete()
        return Response(status=204)


class TimetableList(APIView):
    def get(self, request, format=None):
        timetable_list = Timetable.objects.filter(user__nickname=request.GET['nickname'])
        serializer = TimetableListSerializer(timetable_list, many=True)
        return Response(serializer.data, status=200)









