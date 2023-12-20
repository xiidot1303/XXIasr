import requests
from django.contrib import messages
from .models import Notes, Profile, Upload, Client, SMStext
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.decorators import login_required
from base.utils.message import *
from base.utils.services import create_key


@login_required(login_url='login')
def cancelService(request, pk):
    try:
        obj = Upload.objects.get(id=pk)
    except:
        obj = False
    profile = Profile.objects.get(user= request.user)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Xizmat bekor qilindi :)")
        return redirect("home")
    return render(request, 'base/cancel.html', {'obj':obj, 'profile':profile})

@login_required(login_url='login')
def confirmSerivce(request, pk):
    pk = int(pk)
    profile = Profile.objects.get(user=request.user)
    try:
        obj = Upload.objects.get(id=pk)
    except:
        obj = ""
        return render(request, 'error-404.html')
    if profile.status == 'admin' or profile.status == 'superuser' or obj.reciever == profile:
        if request.method == "POST":
            redirect_url = request.POST['redirect_url'] if 'redirect_url' in request.POST else 'home'
            if obj.status == '0':
                obj.payment = request.POST['price']
                obj.status = '5'
                obj.save()
                
                shablon = SMStext.objects.get(id=3).text
                text = shablon.replace("**nom", obj.reciever.name)
                rephone = obj.reciever.phone
                numberid = rephone
                url = 'http://91.204.239.44/broker-api/send'
                headers = {'Content-type': 'application/json',  # Определение типа данных
                        'Accept': 'text/plain',
                        'Authorization': 'Basic eHhpYXNyOmJwOWJFTVA3ODI='}
                data = {
                "messages":
                [
                {
                "recipient":numberid,
                "message-id":"prime000019953",
    
                    "sms":{
    
                    "originator": "21ASR",
                    "content": {
                    "text": text
                    }
                    }
                        }
                    ]
                } 

                # requests.post(url, json=data, headers=headers) # dont send sms to staffs

                messages.success(request, "Xizmat narxlandi :)")
                return redirect(redirect_url)
            elif obj.status == '5':
                obj.status = '10'
                obj.save()
                shablon = SMStext.objects.get(id=1).text
                text = shablon.replace("**nom", obj.client.name)
                rephone = obj.client.phone1
                numberid = rephone
                url = 'http://91.204.239.44/broker-api/send'
                headers = {'Content-type': 'application/json',  # Определение типа данных
                        'Accept': 'text/plain',
                        'Authorization': 'Basic eHhpYXNyOmJwOWJFTVA3ODI='}
                data = {
                "messages":
                [
                {
                "recipient":numberid,
                "message-id":"prime000019953",
    
                    "sms":{
    
                    "originator": "21ASR",
                    "content": {
                    "text": text
                    }
                    }
                        }
                    ]
                } 
                
                requests.post(url, json=data, headers=headers)
                # send message to client via telegram bot
                bot_send_message(obj.client, text)
        
                messages.success(request, "Xizmat tugatildi :)")
                return redirect(redirect_url)
            else:
                return render(request, 'error-404.html')
        return render(request, 'base/confirm.html', {'obj':obj, 'profile':profile, 'redirect_url': request.META.get('HTTP_REFERER')})
    else:
        return render(request, 'error-404.html')

@login_required(login_url='login')
def editClient(request, pk):
    client = Client.objects.get(id=pk)
    profile=Profile.objects.get(user=request.user)
    if client.type == 'ytt':
        form = YaTTCreation(instance=client)
        if request.method == "POST":
            form = YaTTCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                if client.sub_type == 'aylanma':
                    client.congragulate = True
                else:
                    client.congragulate = False
                client.save()
                form.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('yatt')
            else:
                messages.error(request, "Qandaydir xatolik :(")
    elif client.type == 'yuridik':
        form = YuridikCreation(instance=client)
        if request.method == "POST":
            form = YuridikCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                if client.yuridik_type == 'buxgalteriya':
                    client.congragulate = True
                else:
                    client.congragulate = False
                client.save()
                form.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('yuridik')
            else:
                messages.error(request, "Qandaydir xatolik :(")

    elif client.type == 'jismoniy':
        form = JismoniyCreation(instance=client)
        if request.method == "POST":
            form = JismoniyCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('jismoniy')
            else:
                messages.error(request, "Qandaydir xatolik :(")

    elif client.type == 'taxi':
        form = TaxiCreation(instance=client)
        if request.method == "POST":
            form = TaxiCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('taxi')
            else:
                messages.error(request, "Qandaydir xatolik :(")

    elif client.type == 'ishonchnoma':
        form = IshonchnomaCreation(instance=client)
        if request.method == "POST":
            form = IshonchnomaCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                client = form.save(commit=False)
                files = request.FILES.getlist('ishonchnoma_files')
                for file in files:
                    # file_obj = File.objects.create(file=file)
                    client.ishonchnoma_files.create(ishonchnoma=file)
                # form.save()
                client.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('ishonchnoma')
            else:
                messages.error(request, "Qandaydir xatolik :(")

    elif client.type == 'governor':
        form = GovernorCreation(instance=client)
        if request.method == "POST":
            form = GovernorCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('governor')
            else:
                messages.error(request, "Qandaydir xatolik :(")

    elif client.type == 'tanirovka':
        form = TanirovkaCreation(instance=client)
        if request.method == "POST":
            form = TanirovkaCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('tanirovka')
            else:
                messages.error(request, "Qandaydir xatolik :(")

    elif client.type == 'auction':
        form = AuctionCreation(instance=client)
        if request.method == "POST":
            form = AuctionCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('auction')
            else:
                messages.error(request, "Qandaydir xatolik :(")

    elif client.type == 'auction2':
        form = Auction2Creation(instance=client)
        if request.method == "POST":
            form = Auction2Creation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('auction2')
            else:
                messages.error(request, "Qandaydir xatolik :(")

    elif client.type == 'teacher':
        form = TeacherCreation(instance=client)
        if request.method == "POST":
            form = TeacherCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('teacher')
            else:
                messages.error(request, "Qandaydir xatolik :(")
                
    elif client.type == 'aviakassa':
        form = AviakassaCreation(instance=client)
        if request.method == "POST":
            form = AviakassaCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('aviakassa')
            else:
                messages.error(request, "Qandaydir xatolik :(")
    
    elif client.type == 'daromad12':
        form = Daromad12Creation(instance=client)
        if request.method == "POST":
            form = Daromad12Creation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                client = form.save(commit=False)
                files = request.FILES.getlist('application_files')
                for file in files:
                    client.application_files.create(application=file)
                # form.save()
                client.save()
                create_key(client.pk, profile)
                messages.success(request, "Malumotlar yangilandi")
                return redirect('daromad12')
            else:
                messages.error(request, "Qandaydir xatolik :(")
    
    elif client.type == 'taxer':
        form = TaxerCreation(instance=client)
        if request.method == "POST":
            form = TaxerCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                messages.success(request, "Malumotlar yangilandi")
                return redirect('taxer')
            else:
                messages.error(request, "Qandaydir xatolik :(")
    
    context = {'form':form, 'client': client}
    return render(request, 'base/forms.html', context)

def NotesPage(request):
    form = NotesCreation()
    profile = Profile.objects.get(user=request.user)
    notes = Notes.objects.all()
    if 'filter' in request.GET:
        date_from = request.GET['from']
        if not date_from:
            date_from = '1000-12-12'
        date_to = request.GET['to']
        if not date_to:
            date_to = '3000-12-12'
        notes = notes.filter(period__range=(date_from, date_to)).order_by('status', 'period')
        status = request.GET['status']
        if status:
            notes = notes.filter(status=status)
    
    if profile.status == 'admin' or profile.status == 'superuser':
        notes = notes.order_by('status', 'period')
    elif profile.status == 'user':
        notes = notes.filter(user=profile).order_by('status', 'period')
    if request.method == "POST":
        form = NotesCreation(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = profile
            note.save()
            messages.success(request, 'Eslatma kiritildi :) .')
            return redirect('notes')
        else:
            messages.error(request, 'Qandaydir xatolik :( .')
            return redirect('notes')
    context = {'form':form, 'notes':notes, 'profile':profile}
    return render(request, 'base/notes.html', context)

def editNote(request, pk):
    profile = Profile.objects.get(user=request.user)
    try:
        note = Notes.objects.get(id=pk)
    except:
        note = False
    
    if note and note.user == profile and note.status != "10":
        if request.method == "POST":
            note.status = request.POST['status']
            note.save()
            messages.success(request, 'Jarayon yakunlandi :) ')
            return redirect('notes')
        return render(request, 'base/editnote.html')
    else:
        return render(request, 'error-404.html')
        
