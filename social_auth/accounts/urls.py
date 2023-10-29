from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserList.as_view()),
    path('current/', views.CurrentUser.as_view()),
]
