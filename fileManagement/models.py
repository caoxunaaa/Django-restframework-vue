import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.models import User


class MyStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


def upload_to(instance, filename):
    if isinstance(filename, str):
        return '/'.join([filename.split('.')[1], filename])


class File(models.Model):
    name = models.CharField(max_length=30)
    file_path = models.FileField(verbose_name='文件', upload_to=upload_to, storage=MyStorage())
    upload_time = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)

    class Meta:
        ordering = ['id']
