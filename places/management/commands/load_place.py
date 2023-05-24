import json
import logging
from urllib.parse import urlparse

from django.db.utils import IntegrityError
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

import requests
from requests import HTTPError
from places.models import Venue, VenuePhoto


logging.basicConfig(level=logging.INFO)


def load_venue_to_db(place_url):
    try:
        response = requests.get(place_url)
        response.raise_for_status()
        new_venue = response.json()
        load_venue(new_venue)

    except HTTPError as http_error:
        logging.info(f'\nHTTP error occurred: {http_error}')

    except IntegrityError as load_error:
        logging.info(f'\nError occurred while adding the venue: {load_error}')

    except json.decoder.JSONDecodeError:
        logging.info('\nError occurred while parsing due to inconsistent url.')
    except KeyError as load_error:
        logging.info(f'\nError occurred while adding venue.\nKey {load_error} missing.')


def load_venue(new_venue):
    venue_title = new_venue['title']
    venue_images = new_venue['imgs']
    venue, venue_created = Venue.objects.update_or_create(
        title=venue_title,
        defaults={
            'description_short': new_venue.get('description_short', ''),
            'description_long': new_venue.get('description_long', ''),
            'lat': new_venue['coordinates']['lat'],
            'lng': new_venue['coordinates']['lng']
        },
    )

    if venue_created:
        logging.info(f'Downloading images of {venue_title} in progress.')
    else:
        logging.info(f'Uploading images of {venue_title} in progress.')

    for image_index, image_url in enumerate(venue_images, start=1):
        image_name = urlparse(image_url).path.split('/')[-1]
        response = requests.get(image_url)
        response.raise_for_status()
        VenuePhoto.objects.update_or_create(
            venue=venue,
            order=image_index,
            defaults={
                'image': ContentFile(response.content, name=image_name)
            },
        )


class Command(BaseCommand):
    help = 'Upload JSON file to DB.'

    def handle(self, *args, **options):
        venue_urls = options['venue_urls']
        for venue_url in venue_urls:
            load_venue_to_db(venue_url)

    def add_arguments(self, parser):
        parser.add_argument(
            '-path',
            '--venue_urls',
            help='Enter place json urls',
            nargs='+',
        )
