from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import TemplateView, LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'
    redirect_authenticated_user = True 
    success_url = reverse_lazy('home') 

    def get_success_url(self):
        return self.success_url or self.get_redirect_url() or reverse_lazy('home')
    
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'user/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    
    def get_success_url(self):
        return self.success_url or self.get_redirect_url() or reverse_lazy('home')
