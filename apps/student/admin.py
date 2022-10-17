from django.contrib import admin

from apps.student.models import *

# Register your models here.

admin.site.register(StudentResult)
admin.site.register(Level)
admin.site.register(Criteria)
admin.site.register(LevelDescription)
