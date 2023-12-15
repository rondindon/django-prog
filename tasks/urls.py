from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "tasks"
urlpatterns = [
  path("", views.index, name="index"),
  path("add", views.add, name="add"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)