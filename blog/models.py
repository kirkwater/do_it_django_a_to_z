from django.db import models
import os
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 30) #문자를 담는 필드를 만든다.
    content = models.TextField() #문자열의 길이 제한없는 TextField를 사용해 본문필드 만듬

    created_at = models.DateTimeField(auto_now_add = True) #월,일,시,분,초를 기록할 수 있는
    updated_at = models.DateTimeField(auto_now = True)

    head_image = models.ImageField(upload_to = 'blog/images/%Y/%m/%d/', blank = True) #blank는 null값 드가도 괜찮냐?
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)  # blank는 null값 드가도 괜찮냐?
    # author: 추후 작성 예정
    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]