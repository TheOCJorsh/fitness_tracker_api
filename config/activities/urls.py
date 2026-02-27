from django.urls import path
from .views import ActivityListCreateView, ActivityDetailView, activity_list
from .views import MilestoneListView
from .views import ActivityAnalyticsView

urlpatterns = [
    path('activities/', ActivityListCreateView.as_view(), name='activity-list'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('activities/', activity_list),
    path('milestones/', MilestoneListView.as_view(), name='milestone-list'),
    path('activities/analytics/', ActivityAnalyticsView.as_view(), name='activity-analytics'),
]