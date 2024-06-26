from django.contrib import admin

from .models import Blog, Comment

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment


class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
