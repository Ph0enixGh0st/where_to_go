from django.contrib import admin
from .models import Venue, VenuePhoto
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminBase
from adminsortable2.admin import SortableStackedInline


class PhotoInline(SortableStackedInline):
    model = VenuePhoto
    readonly_fields = ['img_preview', ]
    extra = 1

    def img_preview(self, photo):
        return format_html("<img src={} {}>", mark_safe(photo.image.url), "height=175 width=200")

    img_preview.short_description = 'Image Preview'


@admin.register(Venue)
class VenueAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', )
    inlines = [PhotoInline, ]
