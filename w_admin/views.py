from django.contrib import messages
from django.http.response import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from interviewTest.decorators import user_is_superuser
from interviewTest.models import ClientAccount


@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_superuser, name='dispatch')
class HomePageView(TemplateView):
    template_name = 'w_admin/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['clients'] = ClientAccount.objects.all()
        return context


@login_required
def verify_user(request):
    if request.method == 'POST':
        operation  = request.POST['operation']
        clientid  = request.POST['client_id']
        cl = ClientAccount.objects.get(client_id=int(clientid))
        if operation == 'Approve':
            cl.status = 'Approved'
            cl.is_approved = True
        elif operation == 'Reject':
            cl.status = 'Rejected'
            cl.is_approved = False
        else:
            cl.status = 'Peding'
            cl.is_approved = False
        cl.save()
        messages.success(request, 'Operation performed successfully')
        return HttpResponseRedirect(reverse('w_admin:admin_home'))
