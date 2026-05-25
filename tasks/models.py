from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField(default=timezone.now())
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    def get_id(self):
        return self.id

    @property
    def remaining_days(self):
        now = timezone.now().date()
        delta = self.due_date.date() - now

        return delta.days