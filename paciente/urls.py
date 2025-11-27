from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy

from . import views

app_name = "paciente"

urlpatterns = [
    path("login/", views.login_paciente, name="login"),
    path("dashboard/", views.dashboard_paciente, name="dashboard"),
    path("registrar/", views.registrar_paciente, name="registrar"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="paciente/password_reset_form.html",
                                                                 email_template_name="paciente/password_reset_email.html",
                                                                 success_url=reverse_lazy(
                                                                     "paciente:password_reset_done")),
         name="password_reset"),
    path("password_reset_done/",
         auth_views.PasswordResetDoneView.as_view(template_name="paciente/password_reset_done.html"),
         name="password_reset_done"),

    path("password_reset_confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name="paciente/password_reset_confirm.html", success_url = reverse_lazy("paciente:password_reset_complete")),
         name="password_reset_confirm"),

    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="paciente/password_reset_complete.html"), name="password_reset_complete")
]
