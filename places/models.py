from django.db import models

# Create your models here.


class Venue(models.Model):
    title = models.TextField()
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.DecimalField(max_digits=17, decimal_places=14)
    lat = models.DecimalField(max_digits=17, decimal_places=14)

    def __str__(self):
        return self.title


class VenuePhoto(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='venue_pics', blank=True, null=True)
    order = models.SmallIntegerField('Order #')

    class Meta:
        unique_together = ('venue', 'order', )

    @property
    def show_order_venue(self):
        return f'{self.order}: {self.venue}'

    def __str__(self):
        return f'Photo #{self.order} from {self.venue}'