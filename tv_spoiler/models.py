from django.db import models


class Victim(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    telephone_number = models.CharField(max_length=13, blank=False, null=False)
