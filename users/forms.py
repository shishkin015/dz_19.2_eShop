from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm
from django import forms

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Регистрация пользователя"""

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    """Редактирование пользователя"""

    class Meta:
        model = User
        fields = ('email', 'avatar', 'last_name', 'country', 'phone', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserForgotPasswordForm(StyleFormMixin, PasswordResetForm):
    """Запрос на восстановление пароля"""
    pass


class UserSetNewPasswordForm(StyleFormMixin, SetPasswordForm):
    """Изменение пароля после подтверждения"""
    pass
