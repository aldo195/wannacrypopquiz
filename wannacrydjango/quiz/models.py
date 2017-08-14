import uuid
from django.db import models

ROLE_CHOICES = [
    ('1', 'IT Manager'),
    ('2', 'Executive'),
    ('3', 'Other'),
]

HAVE_REPORT = [
    ('1', "I have a report, let's continue."),
    ('2', "I don't have a report like this."),
]


class Drill(models.Model):
    drill_id = models.CharField(max_length=500, primary_key=True, blank=True, unique=True, default=uuid.uuid4)

    # Result Fields
    risk = models.CharField(max_length=500, default=1, blank=True)
    reason = models.CharField(max_length=500, default=1, blank=True)

    # Vulnerability Management - Workstation Inventory
    workstation_count_estimate = models.CharField(max_length=500, blank=True)
    has_report = models.CharField(max_length=500, choices=HAVE_REPORT, blank=True, default=HAVE_REPORT[0][0])
    workstation_count_active = models.CharField(max_length=500, blank=True)
    workstation_count_auth = models.CharField(max_length=500, blank=True)
    active_percent = models.CharField(max_length=500, blank=True)
    auth_percent = models.CharField(max_length=500, blank=True)

    # Vulnerability Management - Notorious Vulnerabilities
    wannacry_count = models.CharField(max_length=500, blank=True)
    doublepulsar_count = models.CharField(max_length=500, blank=True)
    heartbleed_count = models.CharField(max_length=500, blank=True)
    shellshock_count = models.CharField(max_length=500, blank=True)
    mirai_count = models.CharField(max_length=500, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.drill_id
