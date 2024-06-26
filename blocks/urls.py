from django.urls import path

from .views import ClonePage, IndexPage, ShowTemplates, slug_router

urlpatterns = [
    path("", IndexPage.as_view()),
    path("<slug>", slug_router),
    path("templates/get", ShowTemplates.as_view()),
    path("page/clone", ClonePage.as_view()),
]
