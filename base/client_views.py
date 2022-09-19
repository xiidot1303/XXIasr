from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Client, Profile, Access, Upload
from django.contrib.auth.decorators import login_required

def singleClient(request, pk):
    profile = Profile.objects.get(user=request.user)
    key_access = Access.objects.get(name="key")
    if profile in key_access.user.all():
        access = True
    else:
        access = False
    try:
        client = Client.objects.get(id=pk)
        uploads = Upload.objects.filter(client=client)
        view = True
    except:
        view = False

    if view == True:
        context = {'client':client, 'profile':profile, 'access':access, 'uploads':uploads}
        return render(request, 'base/single-client.html', context)
    else:
        return render(request, 'error-404.html')


def change_congragulation(request, client_pk, status):
    client = Client.objects.get(pk=client_pk)
    if status == 'on':
        client.congragulate = True
    elif status == 'off':
        client.congragulate = False
    client.save()
    return redirect(singleClient, pk=client_pk)

