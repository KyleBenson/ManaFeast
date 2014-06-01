from donations.models import DonationForm
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.gis.geos import Point
import os.path
import uuid


def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        print request.POST
        if form.is_valid():
            new_donation = form.save(commit=False)
            new_donation.user = request.user
            new_donation.location = Point(float(request.POST['lat']), float(request.POST['lon']))

            # handle picture
            for f in request.FILES:
                ext = f.name.split('.')[-1]
                filename = "%s.%s" % (uuid.uuid4(), ext)
                destination = open(os.path.join(settings.MEDIA_ROOT, filename), 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()

            new_donation.save()

            return HttpResponse('<h1>Donation received successfully!</h1>')
        else:
            return HttpResponse('<h1>Error creating donation!</h1>')

    else:
        return HttpResponseRedirect('/static/donation.html')


def search(request):
    return HttpResponseRedirect('/static/map.html')
