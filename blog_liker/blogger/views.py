from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Like


@login_required
def blogs(request):
    blog_list = Blog.objects.all().order_by("-created_at")  # newest first
    paginator = Paginator(blog_list, 10)  # 10 blogs per page

    page_number = request.GET.get("page")  # ?page=2
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "blogger/blogs.html", context)


@login_required
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    total_likes = blog.total_likes()
    user_has_liked = Like.objects.filter(user=request.user, blog=blog).exists()

    context = {
        "blog": blog,
        "total_likes": total_likes,
        "user_has_liked": user_has_liked,
    }
    return render(request, "blogger/blog_detail.html", context)


@login_required
def toggle_like(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    like, created = Like.objects.get_or_create(user=request.user, blog=blog)

    if not created:
        # User already liked → unlike (delete the like)
        like.delete()
    # If created = True, the like was just added
    return redirect("blogger:blog_detail", blog_id=blog.id)
