from django.db import models
from django.utils import timezone
from datetime import timedelta


# Create your models here.
class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_id(self):
        return self.id


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    due_date = models.DateField(default=timezone.now())
    completed = models.BooleanField(default=False)

    category = models.ForeignKey(
        to=Category,
        verbose_name=("Categories"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    def get_id(self):
        return self.id

    @property
    def remaining_days_value(self):
        now = timezone.now().date()
        delta = self.due_date - now

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
