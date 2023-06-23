from django.shortcuts import render


def home(request):
    ctx = {

    }
    return render(request, 'home/index.html', ctx)


def about(request):
    ctx = {

    }
    return render(request, 'home/about.html', ctx)
