import requests
from django.contrib import messages
from .models import Notes, Profile, Upload, Client, SMStext
from django.shortcuts import redirect, render
from .forms import AuctionCreation, JismoniyCreation, NotesCreation, TanirovkaCreation, TeacherCreation, YaTTCreation, YuridikCreation
from django.contrib.auth.decorators import login_required


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
    profile = Profile.objects.get(user=request.user)
    try:
        obj = Upload.objects.get(id=pk)
    except:
        obj = ""
        return render(request, 'error-404.html')
    if profile.status == 'admin' or profile.status == 'superuser' or obj.reciever == profile:
        if request.method == "POST":
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
                
                requests.post(url, json=data, headers=headers)
                messages.success(request, "Xizmat narxlandi :)")
                return redirect("home")
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
                messages.success(request, "Xizmat tugatildi :)")
                return redirect("home")
            else:
                return render(request, 'error-404.html')
        return render(request, 'base/confirm.html', {'obj':obj, 'profile':profile})
    else:
        return render(request, 'error-404.html')

@login_required(login_url='login')
def editClient(request, pk):
    client = Client.objects.get(id=pk)
    if client.type == 'ytt':
        form = YaTTCreation(instance=client)
        if request.method == "POST":
            form = YaTTCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                messages.success(request, "Malumotlar yangilandi")
                return redirect('yatt')
            else:
                messages.error(request, "Qandaydir xatolik :(")
    elif client.type == 'yuridik':
        form = YuridikCreation(instance=client)
        if request.method == "POST":
            form = YuridikCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
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
                messages.success(request, "Malumotlar yangilandi")
                return redirect('jismoniy')
            else:
                messages.error(request, "Qandaydir xatolik :(")

    elif client.type == 'tanirovka':
        form = TanirovkaCreation(instance=client)
        if request.method == "POST":
            form = TanirovkaCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
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
                messages.success(request, "Malumotlar yangilandi")
                return redirect('auction')
            else:
                messages.error(request, "Qandaydir xatolik :(")

    elif client.type == 'teacher':
        form = TeacherCreation(instance=client)
        if request.method == "POST":
            form = TeacherCreation(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                messages.success(request, "Malumotlar yangilandi")
                return redirect('teacher')
            else:
                messages.error(request, "Qandaydir xatolik :(")

    context = {'form':form}
    return render(request, 'base/forms.html', context)

def NotesPage(request):
    form = NotesCreation()
    profile = Profile.objects.get(user=request.user)
    if profile.status == 'admin' or profile.status == 'superuser':
        notes = Notes.objects.all().order_by('status')
    elif profile.status == 'user':
        notes = Notes.objects.filter(user=profile).order_by('status')
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
    if 'filter' in request.GET:
        date_from = request.GET['from']
        date_to = request.GET['to']
        notes = Notes.objects.filter(period__range=(date_from, date_to)).order_by('status')
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
        
