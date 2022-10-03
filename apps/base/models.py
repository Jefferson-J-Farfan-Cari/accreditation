from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.


class BaseAuditingModel(models.Model):
    state = models.BooleanField('State', default=True)
    create_date = models.DateField('Created Date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Modified Date', auto_now=True, auto_now_add=False)
    historical = HistoricalRecords(user_model="user.User", inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        abstract = True
        verbose_name = 'Model Base'
        verbose_name_plural = 'Model Bases'
