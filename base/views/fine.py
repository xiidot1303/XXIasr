from base.views import *

@login_required(login_url='login')
def fine_list(request):
    profile = Profile.objects.get(user=request.user)
    if profile.status == 'admin' or profile.status == 'superuser':
        fines = Fine.objects.filter().order_by('-date')
    else:
        fines = Fine.objects.filter(Q(staff=profile) | Q(controller=profile)).order_by('-date')

    context = {'profile': profile, 'fines': fines}
    return render(request, 'fine/fine_list.html', context)

class FineCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Fine
    form_class = FineForm
    template_name = 'base/forms.html'
    success_url = '/fine-list'
    login_url = 'login'
    permission_required = 'base.add_fine'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # get current profile
        profile = Profile.objects.get(user = self.request.user)
        form.instance.controller = profile
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['view'] = 'Jarima yaratish'
        return context

class FineEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Fine
    form_class = FineForm
    template_name = 'base/forms.html'
    success_url = '/fine-list'
    login_url = 'login'
    permission_required = 'base.change_fine'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # get current profile
        profile = Profile.objects.get(user = self.request.user)
        form.instance.controller = profile
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['view'] = 'Jarima'
        return context

@login_required(login_url='login')
def fine_acquitted(request, pk):
    obj = Fine.objects.get(pk = pk)
    obj.acquitted = not obj.acquitted
    obj.save()
    return redirect(request.META.get('HTTP_REFERER'))