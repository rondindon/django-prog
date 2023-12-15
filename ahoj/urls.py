from django.urls import path

from . import views

app_name = "ahoj"
urlpatterns = [
  path("", views.ahoj, name="index"),
]