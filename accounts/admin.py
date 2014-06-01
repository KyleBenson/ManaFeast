from django.contrib import admin
from accounts.models import Account, Donor, Recipient

admin.site.register(Account)
admin.site.register(Donor)
admin.site.register(Recipient)
