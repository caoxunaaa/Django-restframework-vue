from rest_framework import viewsets
from rest_framework import mixins
from .serializers import FileSerializer
from .models import File
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt

class FileViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    # def get_permissions(self):
    #     return [permissions.IsAuthenticated()]
    @csrf_exempt
    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
