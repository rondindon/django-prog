from django.urls import path
from . import views  # Import your views module here

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name='greet'),
    path("jurco/", views.jurco, name="jurco"),
    path("david/", views.david, name="david")
]
