# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class CurrentTemp(models.Model):
    temp_id = models.IntegerField(primary_key=True)
    tempc = models.FloatField(blank=True, null=True)
    tempf = models.FloatField(blank=True, null=True)
    timestp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Current Temp: " +str(self.tempc) + "c at " + str(self.timestp)

    class Meta:
        managed = False
        db_table = 'current_temp'


class Temps(models.Model):
    tempc = models.FloatField(blank=True, null=True)
    tempf = models.FloatField(blank=True, null=True)
    timestp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temps'
