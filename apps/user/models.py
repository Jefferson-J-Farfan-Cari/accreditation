from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords

from apps.base.models import BaseAuditingModel


def user_path(instance, filename):
    extension = filename.split('.')[-1]
    name = filename.split('.')[0]
    new_filename = "%s_%s.%s" % (name, instance.username, extension)

    return new_filename


def permission_path(instance, filename):
    extension = filename.split('.')[-1]
    name = filename.split('.')[0]
    new_filename = "%s_%s.%s" % (name, instance.name, extension)


class Permission(BaseAuditingModel):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to=permission_path, null=True, blank=True, verbose_name='icon_permission')
    path = models.CharField(max_length=120, unique=True, blank=True, null=True)
    permission_F = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'permission'
        abstract = False
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'

    def __str__(self):
        return self.name


class Role(BaseAuditingModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True, unique=False)
    permissions = models.ManyToManyField(Permission, blank=True, null=True)

    class Meta:
        db_table = 'role'
        abstract = False
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser=False, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=False)
    email = models.EmailField('Correo Electrónico', max_length=255, unique=True, )
    name = models.CharField('Nombres', max_length=255, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=255, blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    image_user = models.ImageField(upload_to=user_path, null=True, blank=True, verbose_name='foto de perfil')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True, verbose_name='role')
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'
