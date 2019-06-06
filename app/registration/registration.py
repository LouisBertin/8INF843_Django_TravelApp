from django.urls import reverse_lazy
from django.views import generic

from app.registration.CustomUserCreationForm import CustomUserCreationForm


# Signup method
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
