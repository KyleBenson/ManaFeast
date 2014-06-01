from donations.models import DonationForm
from django.http import HttpResponse, HttpResponseRedirect


def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        print request.POST
        if form.is_valid():
            new_donation = form.save(commit=False)
            new_donation.user = request.user
            new_donation.save()

            return HttpResponse('<h1>Donation received successfully!</h1>')
        else:
            return HttpResponse('<h1>Error creating donation!</h1>')

    else:
        return HttpResponseRedirect('/static/donation.html')


def search(request):
    return HttpResponseRedirect('/static/map.html')
