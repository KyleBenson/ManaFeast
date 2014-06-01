from django.shortcuts import render
from donations.models import DonationForm
from django.http import HttpResponse


def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            new_donation = form.save(commit=False)
            new_donation.user = request.user
            new_donation.save()
        else:
            return HttpResponse('<h1>Error creating donation!</h1>')

    else:
        form = DonationForm()

    return render(request, 'donate.html', {
        'form': form
    })
