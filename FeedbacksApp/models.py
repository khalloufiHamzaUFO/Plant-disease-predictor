# In FeedbacksApp/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Feedback(models.Model):
    prevention = models.ForeignKey(
        'PreventionApp.Prevention',  # Ensure this is correct
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )
    content = models.TextField()
    rating = models.PositiveIntegerField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Feedback for {self.prevention.title} (Anonymous)'
