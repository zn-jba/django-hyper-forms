from django.db import models


class FormModel(models.Model):
    name = models.CharField(max_length=255)


class FormField(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    form = models.ForeignKey(FormModel, related_name="fields", on_delete=models.CASCADE)


class FormData(models.Model):
    form_id = models.IntegerField()
    field_id = models.IntegerField()
    value = models.CharField(max_length=255)
    record_id = models.IntegerField()


class FormRecord(models.Model):
    date = models.DateTimeField(auto_now_add=True)


class Participant(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    favorite_book = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def save_to_db(name, age, favorite_book) -> None:
        Participant.objects.create(name=name,
                                   age=age,
                                   favorite_book=favorite_book)

    @staticmethod
    def find_by_id(id_: int) -> "Participant":
        return Participant.objects.filter(id=id_).first()

    @staticmethod
    def find_by_name(name: str) -> "Participant":
        return Participant.objects.filter(name=name).first()

    @staticmethod
    def find_all() -> list["Participant"]:
        return Participant.objects.all()

    @staticmethod
    def find_all_by_name(name: str) -> list["Participant"]:
        return Participant.objects.filter(name=name)

