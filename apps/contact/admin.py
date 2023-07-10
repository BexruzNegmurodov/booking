from django.contrib import admin
from .models import Leave_Message


@admin.register(Leave_Message)
class Leave_MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date')
    search_fields = ('name',)

    def has_add_permission(self, request): # admin panelda qo'shish imkoniyati
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
