from django.db import models

# Create your models here.


class Organization(models.Model):
    title = models.CharField(max_length=255)
    subdivisions = models.ManyToManyField("Subdivision", related_name="subdivisions")


class Subdivision(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    supervisor = models.ForeignKey("Employee", on_delete=models.CASCADE, related_name="supervisor")
    employees = models.ManyToManyField("Employee", related_name="employees")


class Position(models.Model):
    title = models.CharField(max_length=255)


class Cabinet(models.Model):
    title = models.CharField(max_length=10)


class CalendarSkip(models.Model):
    employees = models.ManyToManyField("Employee", related_name="employees")
    date_since = models.DateField()
    date_until = models.DateField(null=True)


class CalendarVacation(models.Model):
    employees = models.ManyToManyField("Employee", related_name="employees")
    date_since = models.DateField()
    date_until = models.DateField(null=True)


class CalendarEducation(models.Model):
    event_id = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="event_id")


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
    status_id = models.ForeignKey("MaterialStatus", on_delete=models.CASCADE, related_name="status_id")
    type_id = models.ForeignKey("MaterialType", on_delete=models.CASCADE, related_name="type_id")
    area_id = models.ForeignKey("MaterialArea", on_delete=models.CASCADE, related_name="area_id")
    author = models.CharField(max_length=255)
    file = models.FileField()


class Education(models.Model):
    materials = models.ManyToManyField("Material", blank=True, related_name="materials")
    education_type_id = models.ForeignKey("EducationType", on_delete=models.CASCADE, related_name="education_type_id")


class EventType(models.Model):
    title = models.CharField(max_length=255)


class Event(models.Model):
    title = models.CharField(max_length=255)
    date_since = models.DateTimeField()
    date_until = models.DateTimeField()
    description = models.TextField(max_length=255)
    status = models.BooleanField()
    responsible_workers = models.ManyToManyField("Employee", related_name="responsible_workers")
    event_type_id = models.ForeignKey("EventType", on_delete=models.CASCADE, related_name="event_type_id")
    education_id = models.ForeignKey("Education", on_delete=models.CASCADE, related_name="education_id")


class EmployeeMoreInfo(models.Model):
    birthday = models.DateField()
    personal_phone = models.CharField(max_length=20)


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    position_id = models.ForeignKey("Position", on_delete=models.CASCADE, related_name="position_id")
    work_phone = models.CharField(max_length=20)
    cabinet_id = models.ForeignKey("Cabinet", on_delete=models.CASCADE, related_name="cabinet_id")
    work_email = models.EmailField(max_length=255)
    boss = models.ForeignKey("Employee", on_delete=models.SET_NULL, related_name="boss", null=True)
    helper = models.ForeignKey("Employee", on_delete=models.SET_NULL, related_name="helper", null=True)
    more_info_id = models.ForeignKey("EmployeeMoreInfo", on_delete=models.SET_NULL, null=True, related_name="more_info")