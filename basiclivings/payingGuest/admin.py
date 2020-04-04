from django.contrib import admin
from .models import *
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'user_id', 'address', 'days_since_posted')
    ordering = ['room_id', 'user_id', 'address', ]


admin.site.register(Amenities)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomImage)
admin.site.register(Watchlist)
admin.site.register(RoomsVendorPayment)
admin.site.register(RoomsBookingDetail)
