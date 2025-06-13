from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = models.TextChoices("Priority", "LOW MEDIUM HIGH")
    PRIORITY_ORDER = {
        "HIGH": 1,
        "MEDIUM": 2,
        "LOW": 3,
    }

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    priority = models.CharField(blank=True, choices=PRIORITY_CHOICES, max_length=10)
    priority_order = models.IntegerField(editable=False)

    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Task"
        ordering = ["is_completed", "priority_order", "-updated_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.priority_order = self.PRIORITY_ORDER.get(self.priority, 4)
        super().save(*args, **kwargs)
