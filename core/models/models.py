from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Organization(models.Model):
    title = models.CharField(max_length=255)
    subdivisions = models.ManyToManyField("Subdivision", related_name="subdivisions", blank=True)


class Subdivision(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    supervisor = models.ForeignKey("Employee", on_delete=models.SET_NULL, related_name="supervisor", null=True)
    employees = models.ManyToManyField("Employee", related_name="subdivision_employees", null=True)
    sub_sub_division = models.ForeignKey("SubSubDivision", on_delete=models.SET_NULL, null=True, blank=True)


class SubSubDivision(models.Model):
    title = models.CharField(max_length=255)

class Position(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.title)


class Cabinet(models.Model):
    title = models.CharField(max_length=10, unique=True)


class CalendarSkip(models.Model):
    employees = models.ManyToManyField("Employee", related_name="calendar_skip_employees")
    date_since = models.DateField()
    date_until = models.DateField(null=True)


class CalendarVacation(models.Model):
    employees = models.ManyToManyField("Employee", related_name="calendar_vacation_employees")
    date_since = models.DateField()
    date_until = models.DateField(null=True)


class CalendarEducation(models.Model):
    event_id = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="event")


class EducationType(models.Model):
    title = models.CharField(max_length=255)


class MaterialStatus(models.Model):
    title = models.CharField(max_length=255)


class MaterialType(models.Model):
    title = models.CharField(max_length=255)


class MaterialArea(models.Model):
    title = models.CharField(max_length=255)


class Material(models.Model):
    title = models.CharField(max_length=255)
    date_aprove = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)
    status_id = models.ForeignKey("MaterialStatus", on_delete=models.CASCADE, related_name="status")
    type_id = models.ForeignKey("MaterialType", on_delete=models.CASCADE, related_name="type")
    area_id = models.ForeignKey("MaterialArea", on_delete=models.CASCADE, related_name="area")
    author = models.CharField(max_length=255)
    file = models.FileField()


class Education(models.Model):
    materials = models.ManyToManyField("Material", blank=True, related_name="materials")
    education_type_id = models.ForeignKey("EducationType", on_delete=models.CASCADE, related_name="education_type")


class EventType(models.Model):
    title = models.CharField(max_length=255)


class Event(models.Model):
    title = models.CharField(max_length=255)
    date_since = models.DateTimeField()
    date_until = models.DateTimeField()
    description = models.TextField(max_length=255)
    status = models.BooleanField()
    responsible_workers = models.ManyToManyField("Employee", related_name="responsible_workers")
    event_type_id = models.ForeignKey("EventType", on_delete=models.CASCADE, related_name="event_type")
    education_id = models.ForeignKey("Education", on_delete=models.CASCADE, related_name="education")


class Employee(AbstractUser):
    patronymic = models.CharField(max_length=255)
    position_id = models.ForeignKey("Position", on_delete=models.SET_NULL, null=True, related_name="position")
    work_phone = models.CharField(max_length=20)
    cabinet_id = models.ForeignKey("Cabinet", on_delete=models.SET_NULL, null=True, related_name="cabinet")
    email = models.EmailField(max_length=255)
    boss_id = models.ForeignKey("Employee", on_delete=models.SET_NULL, related_name="boss", null=True)
    helper_id = models.ForeignKey("Employee", on_delete=models.SET_NULL, related_name="helper", null=True)
    subdivision = models.ForeignKey("SubDivision", on_delete=models.SET_NULL, null=True, related_name="employee_subdivision")
    sub_sub_division = models.ForeignKey("SubSubDivision", on_delete=models.SET_NULL, null=True, related_name="employye_sub_sub_division")
    more_info = models.TextField(max_length=255, null=True)
    birthday = models.DateField()
    personal_phone = models.CharField(max_length=20, null=True)


class DocumentCategory(models.Model):
    title = models.CharField(max_length=255)


class DocumentComment(models.Model):
    document_id = models.ForeignKey("Document", on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("Employee", on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Document(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField("DocumentCategory", blank=True)
    has_comment = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)