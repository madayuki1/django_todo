from django.db import models
from django.utils import timezone
from datetime import timedelta

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
    def remaining_days_value(self):
        now = timezone.now().date()
        delta = self.due_date.date() - now

        return delta.days
    
    @property
    def remaining_days(self):
        if self.completed:
            return "Completed"
        days = self.remaining_days_value

        if days < 0:
            return "Overdue"
        elif days == 0:
            return "Today"
        else:
            return f"{days} Days"