from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from places.models import Venue, VenuePhoto
#from django.http import HttpResponse
from django.urls import reverse


def index(request):

    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    venues = Venue.objects.all()

    for venue in venues:
        places_geojson['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [venue.lng, venue.lat]
                },
                "properties": {
                    "title": venue.title,
                    "placeId": venue.id,
                    "detailsUrl": reverse('venues_all', args=[venue.id])
                }
            }
        )

    return render(request, 'index.html', {'all_venues': places_geojson})


def show_venue(request, venue_id):

    venue_id = int(venue_id)
    venue = get_object_or_404(Venue, pk=venue_id)

    photos = VenuePhoto.objects.filter(venue_id=venue_id)

    details_url = {
            "title": venue.title,
            "imgs": [photo.image.url for photo in photos],
            "description_short": venue.description_short,
            "description_long": venue.description_long,
            "coordinates": {
                "lat": venue.lat,
                "lng": venue.lng
            }
        }

    return JsonResponse(details_url, json_dumps_params={'indent': 4, 'ensure_ascii': False})
