from django_filters.rest_framework import FilterSet, filters
from .models import *


class PostFilter(FilterSet):
    # board = filters.NumberFilter(field_name='board_id')
    board = filters.NumberFilter(method='filter_board')
    profile = filters.NumberFilter(field_name='profile_id')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    contents = filters.CharFilter(field_name='contents', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['board', 'profile', 'title', 'contents']

    def filter_board(self, queryset, board_id, value):
        return queryset.filter(**{
            board_id: value,
        })
