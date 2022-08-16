from django.contrib import admin
from .models import Post, Category
# Register your models here.

admin.site.register(Post)#어드민 사이트에서 포스트를 사용할 수 있게 정의

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)