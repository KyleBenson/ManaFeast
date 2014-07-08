from donations.models import DonationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.gis.geos import Point


def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)

        if form.is_valid():
            # add a few fields before saving
            new_donation = form.save(commit=False)
            new_donation.user = request.user
            new_donation.location = Point(float(request.POST['lat']),
                                          float(request.POST['lon']))
            new_donation.save()

            return HttpResponse('<h1>Donation received successfully!</h1>')
        else:
            return HttpResponse('<h1>Error creating donation!</h1>')

    else:
        return HttpResponseRedirect('/static/donation.html')


def search(request):
    return HttpResponseRedirect('/static/map.html')
