from django.db import models


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=30, default="New Task")
    description = models.CharField(max_length=255, default="", blank=True)
    state = models.BooleanField(default=False)

    def __str__(self):
        return f"task {self.name}"

    class Meta:
        db_table = "tasks"
