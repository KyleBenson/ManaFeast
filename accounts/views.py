from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from accounts.models import Account, AccountCreationForm
from django.contrib.auth import authenticate, login


def new_account(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username,
                                password=password)
            login(request, user)
            Account.objects.create(phone_number=form.cleaned_data['phone_number'], user=user)
            return HttpResponseRedirect('static/thanks.html')
        else:
            return HttpResponse('<h1>Error creating user!</h1>')
    else:
        form = AccountCreationForm()

        return render(request, 'new_account.html', {
            'form': form,
        })
