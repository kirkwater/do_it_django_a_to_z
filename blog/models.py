from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 30) #문자를 담는 필드를 만든다.
    content = models.TextField() #문자열의 길이 제한없는 TextField를 사용해 본문필드 만듬

    created_at = models.DateTimeField(auto_now_add = True) #월,일,시,분,초를 기록할 수 있는
    updated_at = models.DateTimeField(auto_now = True)
    # author: 추후 작성 예정
    def __str__(self):
        return f'[{self.pk}] {self.title}'