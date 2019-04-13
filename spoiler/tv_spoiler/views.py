import africastalking
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from .forms import VictimForm, SpoilForm
from .tasks import send_sms, send_welcome_message

# Create your views here.


class HomeView(FormView):
    template_name = 'home.html'
    form_class = VictimForm
    success_url = '/'

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'Spoilers will automatically be sent to your victim after the next episode airs')
            send_welcome_message.delay(form.cleaned_data['telephone_number'])
            return self.form_valid(form)
        else:
            messages.success(request,
                             'Spoilers will automatically be sent to your victim after the next episode airs')
            return self.form_invalid(form)


class SpoilView(FormView):
    template_name = 'spoil.html'
    form_class = SpoilForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            send_sms.delay(form.cleaned_data['spoil_text'])
            return self.form_valid(form)
        else:
            return self.form_invalid(form)





