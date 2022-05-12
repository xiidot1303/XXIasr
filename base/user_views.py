import profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from base.forms import ProfileCreation
from base.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

@login_required(login_url='login')
def Profiles(request):
    profile = Profile.objects.get(user=request.user)
    if profile.status == 'admin':
        profiles= Profile.objects.all()
        return render(request, 'base/profiles.html', {'profiles':profiles, 'profile':profile})
    else:
        return render(request, 'error-404.html')

@login_required(login_url='login')
def CreateProfile(request):
    form = ProfileCreation()
    profile = Profile.objects.get(user=request.user)
    if profile.status == 'admin':
        if request.method == "POST":
            username = request.POST['name']
            password = request.POST['password']
            username = username.replace("'","").replace("`","").lower().replace(" ", "")
            u = User.objects.create_user(username, 'admin@admin.com', password)
            u.first_name = request.POST['name']
            u.save()
            form = ProfileCreation(request.POST, request.FILES)
            user = form.save(commit=False)
            user.user = u
            user.password = password
            user.save()
            messages.success(request, 'Xodim qo\'shildi')
            return redirect('users')
        return render(request, 'base/forms.html', {'view':'createuser', 'form':form, 'profile':profile})
    else:
        return render(request, 'error-404.html')

@login_required(login_url='login')
def DeleteProfile(request, pk):
    profile = Profile.objects.get(user=request.user)
    obj = Profile.objects.get(id=pk)
    user = User.objects.get(username=obj.user)
    if profile.status == 'admin' and obj.status != 'admin':
        if request.method == "POST":
            obj.delete()
            user.delete()
            messages.success(request, 'Xodim o\'chirildi :)')
            return redirect('users')
        return render(request, 'base/delete.html', {'view':'deleteuser', 'profile':profile, 'obj':obj})
    else:
        return render(request, 'error-404.html')

@login_required(login_url='login')
def EditProfile(request, pk):
    profile = Profile.objects.get(user=request.user)
    if profile.status == 'admin':
        obj = Profile.objects.get(id=pk)
        user = User.objects.get(username=obj.user.username)
        form = ProfileCreation(instance=obj)
        if request.method == "POST":
            username = request.POST['name']
            password = request.POST['password']
            username = username.replace("'","").replace("`","").lower().replace(" ", "")
            user.username = username
            user.set_password(password)
            user.save()
           
            form = ProfileCreation(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, 'Ma\'lumotlar yangilandi :) ')
                return redirect('users')
            else:
                messages.error(request, 'Qandaydir xatolik ;( ')

        return render(request, 'base/forms.html', {'view':'createuser', 'form':form, 'profile':profile})
    else:
        return render(request, 'error-404.html')
