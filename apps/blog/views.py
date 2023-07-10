from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Blog, Tags, Comment
from .forms import CommentForm


def blog(request):
    blog_list = Blog.objects.order_by('-id')
    tag = request.GET.get('tag')
    if tag:
        blog_list = blog_list.filter(tags__name__exact=tag)
    paginator = Paginator(blog_list, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    new = Blog.objects.order_by('-id')[:3]
    tags = Tags.objects.all()
    ctx = {
        'objects': page_obj,
        'new': new,
        'tags': tags
    }

    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, **kwargs):
    day = kwargs.get('day')
    month = kwargs.get('month')
    year = kwargs.get('year')
    slug = kwargs.get('slug')
    obj = Blog.objects.get(created_date__day=day, created_date__month=month, created_date__year=year, slug=slug)
    new = Blog.objects.order_by('-id')[:3]
    tags = Tags.objects.all()
    reply_to_comment = Comment.objects.filter(reply_comment__isnull=True, blog_id=obj.id)
    reply = request.GET.get('reply_to_comment')
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = obj
            comment.reply_comment_id = reply
            comment.save()
            return redirect(".")
    ctx = {
        'obj': obj,
        'new': new,
        'tags': tags,
        'form': form,
        "reply_to_comment": reply_to_comment
    }
    return render(request, 'blog/single-blog.html', ctx)
