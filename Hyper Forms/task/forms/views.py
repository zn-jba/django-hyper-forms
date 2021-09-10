from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from .forms import RegisterForm


class IndexView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "forms/index.html")


class RegisterView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "forms/register.html", {"form": RegisterForm()})

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            favorite_book = form.cleaned_data["favorite_book"]

            print(f"name: {name}")
            print(f"age: {age}")
            print(f"favorite_book: {favorite_book}")

        return redirect("/register/")
