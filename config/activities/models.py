from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):

    ACTIVITY_TYPES = [
        ('run', 'Running'),
        ('walk', 'Walking'),
        ('gym', 'Gym'),
        ('cycle', 'Cycling'),
        ('yoga', 'Yoga'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='activities'
    )

    activity_type = models.CharField(
        max_length=20,
        choices=ACTIVITY_TYPES
    )

    duration_minutes = models.PositiveIntegerField()

    distance_km = models.FloatField(
        null=True,
        blank=True
    )

    calories_burned = models.PositiveIntegerField()

    activity_date = models.DateField()

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-activity_date']
        indexes = [
            models.Index(fields=['activity_date']),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"