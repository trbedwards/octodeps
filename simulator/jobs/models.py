from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=80, default='')