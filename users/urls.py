from django.urls import path

from . import views


app_name = "users"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/edit/", views.edit, name="edit"),    
    path("add/", views.add, name="add"),
]