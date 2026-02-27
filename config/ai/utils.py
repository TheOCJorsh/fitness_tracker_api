from django.db.models import Sum, Count
from datetime import date, timedelta

from activities.models import Activity
from activities.utils import calculate_streak


def generate_workout_insight(user):

    today = date.today()

    week_ago = today - timedelta(days=7)

    activities = Activity.objects.filter(
        user=user,
        activity_date__range=(week_ago, today)
    )

    total_activities = activities.count()

    total_calories = activities.aggregate(
        Sum('calories_burned')
    )['calories_burned__sum'] or 0

    total_distance = activities.aggregate(
        Sum('distance_km')
    )['distance_km__sum'] or 0

    streak = calculate_streak(user)

    insight_parts = []

    # Activity frequency insight
    if total_activities == 0:
        insight_parts.append(
            "You have not worked out this week. Starting small can build momentum."
        )

    elif total_activities < 3:
        insight_parts.append(
            f"You worked out {total_activities} times this week. Increasing frequency will improve results."
        )

    else:
        insight_parts.append(
            f"Great job! You worked out {total_activities} times this week."
        )

    # Calories insight
    if total_calories > 0:
        insight_parts.append(
            f"You burned {total_calories} calories."
        )

    # Distance insight
    if total_distance > 0:
        insight_parts.append(
            f"You covered {total_distance:.1f} km."
        )

    # Streak insight
    if streak >= 3:
        insight_parts.append(
            f"You are on a {streak}-day streak. Consistency is key!"
        )

    return " ".join(insight_parts)