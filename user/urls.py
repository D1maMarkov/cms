from django.urls import path

from user.views.auth import LoginView, Logout, RegisterUser, SetToken
from user.views.email import ConfirmEmail, ConfirmNewEmail
from user.views.ideas import (
    AddIdeaView,
    DeleteIdeaView,
    GetIdeasView,
    LikeView,
    UpdateIdea,
)
from user.views.password import ResetPassword, SendMailToResetPassword, SetPassword
from user.views.views import DeleteUserProduct, GetUserInfo

urlpatterns = [
    path("register", RegisterUser.as_view()),
    path("password", SetPassword.as_view()),
    path("password/<str:token>", ResetPassword.as_view()),
    path("login", LoginView.as_view()),
    path("get-user-info", GetUserInfo.as_view()),
    path("confirm-email/<str:token>", ConfirmEmail.as_view()),
    path("confirm-new-email/<str:token>", ConfirmNewEmail.as_view()),
    path("reset-password", SendMailToResetPassword.as_view()),
    path("set-token/<str:token>", SetToken.as_view()),
    path("delete-user-product", DeleteUserProduct.as_view()),
    path("logout", Logout.as_view()),
    path("idea", AddIdeaView.as_view()),
    path("update-idea", UpdateIdea.as_view()),
    path("delete-idea", DeleteIdeaView.as_view()),
    path("ideas", GetIdeasView.as_view()),
    path("like", LikeView.as_view()),
]
