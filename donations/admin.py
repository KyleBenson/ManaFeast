from django.contrib import admin
from donations.models import Donation

class DonationAdmin(admin.ModelAdmin):
        list_display = ('short_description', 'user', 'food_type')

admin.site.register(Donation, DonationAdmin)
