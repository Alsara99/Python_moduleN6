from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.contrib.auth import login
from .forms import CustomUserCreationForm

class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user_email]
        send_mail(subject, message, 'nelysisgk@yandex.ru', recipient_list)