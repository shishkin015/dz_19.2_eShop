from django.urls import path

from users.apps import UsersConfig
from users.services import generate_password
from users.views import RegisterView, ProfileView, LoginView, LogoutView, UserForgotPasswordView, \
    UserPasswordResetConfirmView

app_name = UsersConfig.name


# <uidb64>/<token> - это необходимый токен для подтверждения пользователя для смены пароля,
# который придет на email адрес

urlpatterns = (
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword', generate_password, name='generate_password'),
    path('password_reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set_new_password/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
)
