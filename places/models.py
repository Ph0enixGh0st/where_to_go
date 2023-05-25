from django.db import models
from tinymce.models import HTMLField
from django.db.models import TextField


class Venue(models.Model):
    title = models.CharField(max_length=150)
    description_short = TextField(verbose_name='Short description', blank=True)
    description_long = HTMLField(verbose_name='Long description', blank=True)
    lng = models.DecimalField(max_digits=17, decimal_places=14)
    lat = models.DecimalField(max_digits=17, decimal_places=14)

    def __str__(self):
        return self.title


class VenuePhoto(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='venue_pics')
    order = models.PositiveIntegerField('Order #', null=True, blank=True)

    class Meta:
        ordering = ('order', )

    @property
    def show_order_venue(self):
        return f'{self.order}: {self.venue}'

    def __str__(self):
        return f'Photo #{self.order} from {self.venue}'
