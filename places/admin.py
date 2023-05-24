from django.contrib import admin
from .models import Venue, VenuePhoto
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminBase
from adminsortable2.admin import SortableStackedInline


class PhotoInline(SortableStackedInline):
    model = VenuePhoto
    readonly_fields = ['preview_img', ]
    extra = 1

    def preview_img(self, photo):
        return format_html('<img src={} {}>', photo.image.url, 'height=200')

    preview_img.short_description = 'Image Preview'


@admin.register(Venue)
class VenueAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', )
    inlines = [PhotoInline, ]
