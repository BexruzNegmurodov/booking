from django.contrib import admin
from .models import RoomService, Room, RoomImage, RoomReview, Booking


@admin.register(RoomService)
class RoomServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modified_date', 'created_date')
    readonly_fields = ('modified_date', 'created_date')
    list_filter = ('created_date', )
    search_fields = ('name', )


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 0

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = (RoomImageInline, )
    list_display = ('id', 'name', 'size', 'capacity', 'price', 'modified_date', 'created_date')
    list_filter = ('created_date', 'capacity')
    readonly_fields = ('modified_date', 'created_date')
    search_fields = ('name', )
    filter_horizontal = ('services', )


@admin.register(RoomReview)
class RoomReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mark', 'modified_date', 'created_date')
    list_filter = ('created_date', 'mark')
    readonly_fields = ('modified_date', 'created_date')
    search_fields = ('name', )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'client_phone', 'room', 'check_in', 'check_out', 'days', 'peer_day', 'total', 'created_date')
    list_filter = ('created_date', 'room')
    readonly_fields = ('created_date', )
    search_fields = ('client_name', 'client_phone')

    def peer_day(self, obj):
        return obj.room.price


