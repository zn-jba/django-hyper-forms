from django.db import models

# NOTES
# The get method always returns an instance of a particular mode
# The filter method returns the QuerySet

#  the filter method returns the QuerySetQuerySet is a wrapper for a
#  set of objects in the database. QuerySet and Manager have much in
#  common, so you can easily convert one into another. You can think of
#  QuerySet as of another type of Manager.


class Participant(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    favorite_book = models.CharField(max_length=255)

    def create(self, name: str) -> "Participant":
        return Participant.objects.create(name=name)

    def find_by_id(self, id_: int) -> "Participant":
        return Participant.objects.filter(id=id_).first()

    def find_by_name(self, name: str) -> "Participant":
        # filter() is safer than get()
        # TODO: if has_attr else raise Exception
        return Participant.objects.filter(name=name).first()
        # try:
        #     return Participant.objects.get(name=name)
        # except Participant.DoesNotExist:
        #     pass

    def find_all(self) -> list["Participant"]:
        # return Participant.objects.get()
        return Participant.objects

    def find_all_by_name(self, name: str) -> list["Participant"]:
        return Participant.objects.filter(name=name)
