from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        task = request.POST.get("todo")
        if task and task not in self.all_todos:
            self.all_todos.append(task)
        return redirect("/")
