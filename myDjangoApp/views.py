from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .serializers import BookSerializer
from .models import Book
from rest_framework import status
from rest_framework.response import Response


class BookViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

