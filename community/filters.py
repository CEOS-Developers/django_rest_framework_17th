from django_filters.rest_framework import FilterSet, filters
from .models import *


class PostFilter(FilterSet):
    # board = filters.NumberFilter(field_name='board_id')
    board = filters.NumberFilter(method='filter_board')
    # profile = filters.NumberFilter(field_name='profile_id')
    profile = filters.NumberFilter(method='filter_profile')
    # title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    title = filters.CharFilter(method='filter_title')
    # contents = filters.CharFilter(field_name='contents', lookup_expr='icontains')
    contents = filters.CharFilter(method='filter_contents')

    class Meta:
        model = Post
        fields = ['board', 'profile', 'title', 'contents']

    # def filter_board(self, queryset, board_id, value):
    #     return queryset.filter(**{
    #         board_id: value,
    #     })

    def filter_board(self, queryset, board_id, value):
        return queryset.filter(board_id=value, deleted_at__isnull=True)

    def filter_profile(self, queryset, profile_id, value):
        return queryset.filter(profile_id=value, deleted_at__isnull=True)

    def filter_title(self, queryset, title, value):
        return queryset.filter(title__icontains=value, deleted_at__isnull=True)

    def filter_contents(self, queryset, contents, value):
        return queryset.filter(contents__icontains=value, deleted_at__isnull=True)
