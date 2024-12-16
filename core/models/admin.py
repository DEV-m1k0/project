from django.contrib import admin
from models.models import *

# Register your models here.

admin.site.register(Employee)
admin.site.register(Document)
admin.site.register(DocumentComment)