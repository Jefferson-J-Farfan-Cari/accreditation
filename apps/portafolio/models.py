from django.db import models
from apps.base.models import BaseAuditingModel
from apps.user.models import User
from apps.course.models import PeriodAcademic, Course


def file_path(instance, filename):
    extension = filename.split('.')[-1]
    name = filename.split('.')[0]
    new_filename = "%s/file_%s.%s" % (extension, instance.course.name+"_"+instance.period_academic.year+"-"+instance.period_academic.period+"_"+name+"_"+str(instance.id), extension)
    return new_filename


class Professor(BaseAuditingModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    period = models.ForeignKey(PeriodAcademic, on_delete=models.CASCADE, blank=False, null=False)
    courses = models.ManyToManyField(Course, blank=True, symmetrical=False)

    class Meta:
        db_table = 'professor'
        abstract = False
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

    def __str__(self):
        return str(self.user_id)


class Task(BaseAuditingModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    description = models.CharField(max_length=300, unique=False, blank=True, null=True)
    init_date = models.DateField('Initial Date')
    limit_date = models.DateField('Limit Date')

    class Meta:
        db_table = 'task'
        abstract = False
        verbose_name = 'Task'
        verbose_name_plural = 'Task'

    def __str__(self):
        return str(self.description)


class Stage(BaseAuditingModel):
    name = models.CharField(max_length=120, unique=False, blank=False, null=False)
    period_academic = models.ForeignKey(PeriodAcademic, on_delete=models.CASCADE, blank=False, null=False)
    initial_date = models.DateField('Initial Date')
    limit_date = models.DateField('Limit Date')
    state = models.BooleanField(default=True)

    class Meta:
        db_table = 'stage'
        abstract = False
        verbose_name = 'Stage'
        verbose_name_plural = 'Stages'

    def __str__(self):
        return str(self.name)


class Folder(BaseAuditingModel):
    name = models.CharField(max_length=120, unique=False, blank=False, null=False)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        db_table = 'folder'
        abstract = False
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'

    def __str__(self):
        return str(self.name)


class FileResource(BaseAuditingModel):
    name = models.CharField(max_length=120, unique=False, blank=False, null=False)
    period_academic = models.ForeignKey(PeriodAcademic, on_delete=models.CASCADE, blank=False, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    path = models.FileField(upload_to=file_path, null=False, blank=False, verbose_name='file resource')

    class Meta:
        db_table = 'file_resource'
        abstract = False
        verbose_name = 'File_Resource'
        verbose_name_plural = 'File_Resources'

    def __str__(self):
        return self.name


class Portfolio(BaseAuditingModel):
    resource = models.ForeignKey(FileResource, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'portfolio'
        abstract = False
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        return str(self.pk)


class Form(BaseAuditingModel):
    name = models.CharField(max_length=120, unique=False, blank=False, null=False)
    path = models.CharField(max_length=200, unique=True, blank=False, null=False)
    state = models.BooleanField(default=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        db_table = 'form'
        abstract = False
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'

    def __str__(self):
        return self.name
