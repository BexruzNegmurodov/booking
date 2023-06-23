from django.shortcuts import render

def blog(request):
    ctx = {

    }
    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, slug):
    ctx = {

    }
    return render(request, 'blog/single-blog.html', ctx)

