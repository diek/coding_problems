from django.urls import path

from . import views

app_name = "blogger"

urlpatterns = [
    path("", views.blogs, name="blogs"),  # homepage
    # Blog detail page
    path("blog/<int:blog_id>/", views.blog_detail, name="blog_detail"),
    # Like/unlike action
    path("blog/<int:blog_id>/like/", views.toggle_like, name="toggle_like"),
]
