from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Activity
from .utils import check_and_create_milestones


@receiver(post_save, sender=Activity)
def create_milestones_after_activity(sender, instance, created, **kwargs):
    if created:
        check_and_create_milestones(instance.user)