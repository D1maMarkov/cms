from django.urls import path

from emails.views import SendConfirmEmail

urlpatterns = [
    path("send-confirm-email", SendConfirmEmail.as_view()),
]
