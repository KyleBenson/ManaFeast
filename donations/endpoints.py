from ajax.exceptions import AJAXError
from donations.models import Donation
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from ajax.encoders import encoder


def search(request):
    if request.method == 'POST' and len(request.POST):
        query = request.POST
        print query
        #TODO: fix the JSON in the map.html file so it doesn't wrap each value in a list...
        objs = Donation.objects.filter(
                                       time_window_end__gte=query['time_window_start'][0],
                                       time_window_start__lte=query['time_window_end'][0],
                                       location__distance_lte=(Point(float(query['lat'][0]), float(query['lon'][0])), Distance(mi=query['distance'][0])),
                                       )

        if query['food_type'][0]:
            objs = objs.filter(food_type__in=query['food_type'][0].strip().split())

        # careful here, don't want to use exclude as a donation may have both
        # options.  Note that one of these must be true!
        if not query['pickup'][0] or not query['dropoff'][0]:
            objs = objs.filter(dropoff=True) if not query['pickup'][0] else objs.filter(pickup=True)

        if query['keywords'][0]:
            kw_objs = Donation.objects.none()
            for kw in query['keywords'][0].split():
                kw_objs |= objs.filter(short_description__icontains=kw)
                kw_objs |= objs.filter(long_description__icontains=kw)
            objs = kw_objs

        return encoder.encode(objs)

    else:
        raise AJAXError(500, 'Nothing to echo back.')
