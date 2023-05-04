import django_filters
from django_filters.rest_framework import FilterSet, filters

from .models import *


class PostFilter(FilterSet):

    title = filters.CharFilter(lookup_expr='icontains', field_name='title')
    user = filters.NumberFilter(field_name='user_id')
    board = filters.NumberFilter(field_name='board_id')

    class Meta:
        model = Post
        fields = ['title', 'user', 'board']

