from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        todo = request.POST.get("todo")
        if todo not in self.all_todos:
            important = request.POST.get("important")
            if important:
                self.all_todos.insert(0, todo)
            else:
                self.all_todos.append(todo)
        return redirect("/")
