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
    drill_id = models.CharField(max_length=100, primary_key=True, blank=True, unique=True, default=uuid.uuid4)
    email = models.EmailField(blank=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, blank=True)
    workstation_count_estimate = models.CharField(max_length=10, blank=True)
    has_report = models.CharField(max_length=10, choices=HAVE_REPORT, blank=True, default=HAVE_REPORT[0][0])
    workstation_count_active = models.CharField(max_length=10, blank=True)
    workstation_count_auth = models.CharField(max_length=10, blank=True)
    active_percent = models.CharField(max_length=10, blank=True)
    auth_percent = models.CharField(max_length=10, blank=True)
    risk = models.CharField(max_length=100, default=1, blank=True)
    reason = models.CharField(max_length=300, default=1, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.drill_id
