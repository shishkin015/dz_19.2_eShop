import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse


def generate_password(request):
    new_password = ''.join([str(random.randint(0, 5)) for _ in range(10)])
    send_mail(
        subject='Смена пароля на тестовой платформе',
        message=f'Новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect((reverse('users:login')))
