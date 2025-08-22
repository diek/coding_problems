# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Blog, Like


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "author", "created_at")
    list_filter = ("author", "created_at")
    date_hierarchy = "created_at"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "blog", "created_at")
    list_filter = ("user", "blog", "created_at")
    date_hierarchy = "created_at"
