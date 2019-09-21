from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from . import forms

app_name = "accounts"

urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(template_name="accounts/login.html"), name="login"),
    url(r'^logout/$', logout_then_login, name="logout"),
    url(r'^profile/update/$', views.ProfileUpdateView.as_view(), name="profile_update"),


    url(r"^otp/resend/$", views.otp_resend, name='otp_resend'),

    url(r"^otp/verify/$", views.OTPVerifyView.as_view(), name='otp_verify'),

    url(r"^password/change/$", views.password_change, name='password_change'),

    url(r"^password/reset/$", views.PasswordResetView.as_view(), name='password_reset'),

    url(r"^password/reset/new/$", views.PasswordResetNewView.as_view(), name='password_reset_new'),
    url(r"^password/reset/otp/resend/$", views.password_reset_otp_resend, name='password_reset_otp_resend'),

    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html', authentication_form=forms.CustomLoginForm),
        name='login'),

]
