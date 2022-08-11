from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk' #기본키로 정렬할꺼야 라는 의미.
