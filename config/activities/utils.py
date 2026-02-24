from django.db.models import Sum
from .models import Activity, Milestone
from datetime import timedelta


def calculate_streak(user):

    activities = (
        Activity.objects
        .filter(user=user)
        .order_by('-activity_date')
        .values_list('activity_date', flat=True)
        .distinct()
    )

    if not activities:
        return 0

    streak = 1
    previous_date = activities[0]

    for current_date in activities[1:]:

        if previous_date - current_date == timedelta(days=1):
            streak += 1
            previous_date = current_date
        else:
            break

    return streak

def check_and_create_milestones(user):

    # 1️⃣ Activity Count Milestones
    activity_count = Activity.objects.filter(user=user).count()

    activity_targets = [5, 10, 20]

    for target in activity_targets:
        if activity_count >= target:
            Milestone.objects.get_or_create(
                user=user,
                milestone_type='activity_count',
                value=target
            )
    #  Streak Milestones
    streak = calculate_streak(user)

    streak_targets = [3, 7, 14]

    for target in streak_targets:
        if streak >= target:
            Milestone.objects.get_or_create(
                user=user,
                milestone_type='streak',
                value=target
            )


    # 2️⃣ Total Distance Milestones
    total_distance = Activity.objects.filter(user=user).aggregate(
        total=Sum('distance_km')
    )['total'] or 0

    distance_targets = [50, 100, 200]

    for target in distance_targets:
        if total_distance >= target:
            Milestone.objects.get_or_create(
                user=user,
                milestone_type='distance_total',
                value=target
            )

    # 3️⃣ Total Calories Milestones
    total_calories = Activity.objects.filter(user=user).aggregate(
        total=Sum('calories_burned')
    )['total'] or 0

    calorie_targets = [500, 1000, 5000]

    for target in calorie_targets:
        if total_calories >= target:
            Milestone.objects.get_or_create(
                user=user,
                milestone_type='calories_total',
                value=target
            )