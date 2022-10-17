from django.contrib import admin
from apps.course.models import Department, PeriodAcademic, Course, StudyPlan, Component

admin.site.register(Department)
admin.site.register(PeriodAcademic)
admin.site.register(Course)
admin.site.register(StudyPlan)
admin.site.register(Component)