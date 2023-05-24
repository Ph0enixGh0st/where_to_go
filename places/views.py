from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from places.models import Venue
from django.urls import reverse


def index(request):
    venues = Venue.objects.all()
    features_roster = []
    for venue in venues:
        features = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [venue.lng, venue.lat]
            },
            "properties": {
                "title": venue.title,
                "placeId": venue.id,
                "detailsUrl": reverse("venues_all", args=[venue.id])
            }
        }
        features_roster.append(features)
    places_desc = {
        "type": "FeatureCollection",
        "features": features_roster
    }
    return render(request, "index.html", {"all_venues": places_desc})


def show_venue(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    photos = venue.images.all()
    venue_details = {
        "title": venue.title,
        "imgs": [photo.image.url for photo in photos],
        "description_short": venue.description_short,
        "description_long": venue.description_long,
        "coordinates": {
            "lat": venue.lat,
            "lng": venue.lng
        }
    }
    return JsonResponse(venue_details, json_dumps_params={"indent": 4, "ensure_ascii": False})
