from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .serializers import BookSerializer
from .models import Book
from rest_framework.pagination import PageNumberPagination


class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


class BookViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    lookup_field = 'pk'
