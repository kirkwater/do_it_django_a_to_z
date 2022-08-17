from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs): # **kwargs(딕셔너리형태로 받는다. **은 딕션너리 형태)
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category = None).count()
        return context
def tag_page(request, slug):
    tag = Tag.objects.get(slug = slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'tag': tag,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category = None).count(),
        }
    )
def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category = None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category = category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category = None).count(),
            'category': category,
        }
    )
class PostDetail(DetailView):
    model = Post


    def get_context_data(self, **kwargs): # **kwargs(딕셔너리형태로 받는다. **은 딕션너리 형태)
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category = None).count()
        return context

