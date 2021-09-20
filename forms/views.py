from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from .models import FormData
from .models import FormField
from .models import FormModel
from .models import FormRecord


class IndexView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form_model = FormModel.objects.filter(name="participants").first()

        if not form_model:
            return render(request, "forms/index.html")

        fields = form_model.fields.all()

        records = FormRecord.objects.all()
        form_records = []
        for record in records:
            form_data = FormData.objects.filter(record_id=record.id)

            row = []
            for item in form_data:
                row.append(item.value)

            form_records.append(row)

        return render(request, "forms/index.html", {"fields": fields,
                                                    "form_records": form_records})


class RegisterView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        participants_form = FormModel.objects.filter(name="participants").first()
        fields = None
        if participants_form:
            fields = participants_form.fields.all()
        return render(request, "forms/register.html", {"fields": fields})

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        participant_form = FormModel.objects.filter(name="participants").first()
        form_record_name = FormRecord.objects.create()

        for field_name, field_value in request.POST.items():
            field = FormField.objects.filter(name=field_name).first()
            if field:
                form_data_name = FormData.objects.create(form_id=participant_form.id,
                                                         field_id=field.id,
                                                         value=field_value,
                                                         record_id=form_record_name.id)
                form_data_name.save()

        return redirect("forms:register")
