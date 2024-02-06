from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Client, Profile, Access, Upload
from django.contrib.auth.decorators import login_required
from base.utils.message import *

def singleClient(request, pk):
    if request.method == 'POST':
        data = request.POST
        message = data['message'] or ' '
        client = Client.objects.get(pk=pk)
        via = data['via']
        if via == 'sms' or via == 'both':
            send_sms(client, message)
            messages.success(request, 'Xabar foydalanuvchiga yuborildi')
        if via == 'telegram' or via == 'both':
            send_message = bot_send_message(client, message)
            if send_message == 'success':
                messages.success(request, 'Xabar foydalanuvchiga yuborildi')
            else:
                messages.error(request, 'Foydalanuvchi botga a\'zo emas')
        return redirect(singleClient, pk=pk)

    profile = Profile.objects.get(user=request.user)
    key_access = Access.objects.get(name="key")
    if profile in key_access.user.all():
        access = True
    else:
        access = False
    try:
        client = Client.objects.get(id=pk)
        uploads = Upload.objects.filter(client=client)
        action_histories = ActionHistory.objects.filter(client_id = client.pk)
        view = True
    except:
        view = False

    if view == True:
        context = {'client':client, 'profile':profile, 'access':access, 'uploads':uploads, 'histories': action_histories}
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

