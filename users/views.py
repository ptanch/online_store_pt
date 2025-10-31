from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    """Класс для создания пользователя"""
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Валидация формы"""
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    @staticmethod
    def send_welcome_email(user_email):
        """Отправка приветственного письма"""
        subject = 'Добро пожаловать в наш магазин!'
        message = 'Спасибо, что зарегистрировались в нашем магазине!'
        from_email = EMAIL_HOST_USER
        recepient_list = [user_email]
        send_mail(subject, message, from_email,recepient_list)
