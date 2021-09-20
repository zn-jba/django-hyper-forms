from django.contrib import admin

from .models import FormData
from .models import FormField
from .models import FormModel
from .models import FormRecord
from .models import Participant


class FormDataAdmin(admin.ModelAdmin):
    pass


class FormFieldAdmin(admin.ModelAdmin):
    pass


class FormModelAdmin(admin.ModelAdmin):
    pass


class FormRecordAdmin(admin.ModelAdmin):
    pass


class ParticipantAdmin(admin.ModelAdmin):
    fields = ("name", "age", "favorite_book", "id", "created_on", "trending")
    readonly_fields = ("id", "created_on", "trending")

    def trending(self, obj):
        return 'yes' if obj.age_set.count() >= 30 else 'no'


admin.site.register(FormData, FormDataAdmin)
admin.site.register(FormField, FormFieldAdmin)
admin.site.register(FormModel, FormModelAdmin)
admin.site.register(FormRecord, FormRecordAdmin)
admin.site.register(Participant, ParticipantAdmin)
