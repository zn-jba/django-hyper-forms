from django.urls import path

from .views import IndexView
from .views import RegisterView

app_name = "forms"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("register/", RegisterView.as_view(), name="register"),
]
