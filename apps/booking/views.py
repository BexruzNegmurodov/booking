import datetime

from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Room, RoomReview, Booking
from .forms import RoomReviewForm


def room(request):
    object_list = Room.objects.order_by('-id')
    checkin = request.GET.get('checkin-date')
    checkout = request.GET.get('checkout-date')
    adults = request.GET.get('adults')
    children = request.GET.get('children')
    credentials = [checkin, checkout, adults, children]
    if all(credentials):
        count_person = int(adults) + int(children)
        if checkin > checkout:
            return HttpResponse("checkout must be grater than checkin")
        checkin_lst = checkin.split('-')  # ['2023', '07', '05']
        checkin_date = datetime.date(int(checkin_lst[0]), int(checkin_lst[1]), int(checkin_lst[2]))  # 2023-07-05
        print(checkin_date)
        if checkin_date < datetime.datetime.today().date():
            return HttpResponse("checkin must be grater than today")
        busy_rooms_set = set()

        bookings = Booking.objects.filter(
            check_out__gte=checkin,  # kattaroq
            check_in__lte=checkout  # kichikroq
        ).values_list('room_id', )
        for i in bookings:
            busy_rooms_set.add(i[0])
        object_list = Room.objects.exclude(id__in=busy_rooms_set)

    paginator = Paginator(object_list, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ctx = {
        'objects': page_obj
    }
    return render(request, 'booking/room.html', ctx)


def room_detail(request, **kwargs):
    slug = kwargs.get('slug')
    day = kwargs.get('day')
    month = kwargs.get('month')
    year = kwargs.get('year')
    obj = get_object_or_404(Room, created_date__day=day, created_date__month=month, created_date__year=year, slug=slug)
    review = RoomReview.objects.all()
    form = RoomReviewForm()
    if request.method == "POST":
        form = RoomReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.room = obj
            review.save()
            return redirect(obj.full_url)

    ctx = {
        'obj': obj,
        'form': form,
        "review": review
    }
    return render(request, 'booking/single-room.html', ctx)
