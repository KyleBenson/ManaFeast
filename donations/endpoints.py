from ajax.exceptions import AJAXError
from donations.models import Donation
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from ajax.encoders import encoder


def search(request):
    if request.method == 'POST' and len(request.POST):
        query = request.POST
        objs = Donation.objects.filter(
                                       time_window_end__gte=query['time_window_start'],
                                       time_window_start__lte=query['time_window_end'],
                                       location__distance_lte=(Point(float(query['lat']), float(query['lon'])), Distance(mi=query['distance'])),
                                       )

        if query['food_type']:
            objs = objs.filter(food_type__in=query['food_type'].strip().split())

        # careful here, don't want to use exclude as a donation may have both
        # options.  Note that one of these must be true!
        if not query['pickup'] or not query['dropoff']:
            objs = objs.filter(dropoff=True) if not query['pickup'] else objs.filter(pickup=True)

        if query['keywords']:
            kw_objs = Donation.objects.none()
            for kw in query['keywords'].split():
                kw_objs |= objs.filter(short_description__icontains=kw)
                kw_objs |= objs.filter(long_description__icontains=kw)
            objs = kw_objs

        return encoder.encode(objs)

    else:
        raise AJAXError(500, 'Nothing to echo back.')
