from base.views import *

@login_required
def fine_list(request):
    profile = Profile.objects.get(user=request.user)
    if profile.status == 'admin' or profile.status == 'superuser':
        fines = Fine.objects.filter().order_by('-date')
    else:
        fines = Fine.objects.filter(staff=profile).order_by('-date')
    
    context = {'profile': profile, 'fines': fines}
    return render(request, 'fine/fine_list.html', context)

class FineCreateView(LoginRequiredMixin, CreateView):
    model = Fine
    form_class = FineForm
    template_name = 'base/forms.html'
    success_url = '/fine-list'
    login_url = 'login'
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
        return context