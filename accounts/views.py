from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import StallionUserCreationForm

class SignUpView(CreateView):
    form_class = StallionUserCreationForm
    sucess_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

