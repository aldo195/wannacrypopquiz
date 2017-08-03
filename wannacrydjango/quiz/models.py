import uuid
from django.db import models


class Drill(models.Model):
    email = models.CharField(max_length=100, default="none", blank=True)
    workstation_count_estimate = models.CharField(max_length=10, default="0", blank=True)
    has_report = models.CharField(max_length=10, default="0", blank=True)
    workstation_count_active = models.CharField(max_length=10, default="0", blank=True)
    workstation_count_auth = models.CharField(max_length=10, default="0", blank=True)
    drill_id = models.CharField(max_length=100, primary_key=True, blank=True, unique=True, default=uuid.uuid4)

    def publish(self):
        self.save()

    def __str__(self):
        return self.drill_id
