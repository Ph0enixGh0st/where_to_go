from django.contrib import admin
from .models import Venue, VenuePhoto


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(VenuePhoto)
class VenuePhotoAdmin(admin.ModelAdmin):
    list_display = ('show_order_venue', )
