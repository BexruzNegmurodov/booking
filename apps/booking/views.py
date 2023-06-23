from django.shortcuts import render


def room(request):
    ctx = {

    }
    return render(request, 'booking/room.html', ctx)


def room_detail(request, slug):
    ctx = {

    }
    return render(request, 'booking/single-room.html', ctx)


