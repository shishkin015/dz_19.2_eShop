from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm, UserForgotPasswordForm, UserSetNewPasswordForm
from users.models import User


# Create your views here.

class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    template_name = 'users/login.html'


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Вы зарегистрированы на тестовой платформе',
            message='Успешная регистрация на тестовой платформе',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """Представление по сбросу пароля по почте
    SuccessMessageMixin: - для оповещения пользователя об успешной отправке письма с инструкцией по восстановлению пароля"""
    form_class = UserForgotPasswordForm
    template_name = 'users/user_password_reset.html'
    success_url = reverse_lazy('user:login')
    email_template_name = 'users/email/password_reset_mail.html'
    subject_template_name = 'users/email/password_subject_reset_mail.txt'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Запрос на восстановление'
        return context_data


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """Представление установки нового пароля
    SuccessMessageMixin: -  для оповещения пользователя об успешной смене пароля"""
    form_class = UserSetNewPasswordForm
    template_name = 'users/user_password_set_new.html'
    success_url = reverse_lazy('user:login')
    success_message = 'Пароль изменен. Авторизуйтесь в приложении'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Установить новый пароль'
        return context_data
