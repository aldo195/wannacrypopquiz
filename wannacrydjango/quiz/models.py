import uuid
from django.db import models

ROLE_CHOICES = [
    ('1', 'Outside of IT'),
    ('2', 'IT Manager'),
    ('3', 'IT Executive'),
]

HAVE_REPORT = [
    ('1', "I have a report, let's continue."),
    ('2', "I don't have a report like this."),
]


class Drill(models.Model):
    email = models.EmailField(blank=True)
    role = models.CharField(max_length=100, default=1, choices=ROLE_CHOICES, blank=True)
    workstation_count_estimate = models.CharField(max_length=10, default="0", blank=True)
    has_report = models.CharField(max_length=10, default=1, choices=HAVE_REPORT, blank=True)
    workstation_count_active = models.CharField(max_length=10, default="0", blank=True)
    workstation_count_auth = models.CharField(max_length=10, default="0", blank=True)
    drill_id = models.CharField(max_length=100, primary_key=True, blank=True, unique=True, default=uuid.uuid4)

    def publish(self):
        self.save()

    def __str__(self):
        return self.drill_id
