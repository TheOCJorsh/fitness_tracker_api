from django.urls import path
from .views import ActivityListCreateView, ActivityDetailView, activity_list

urlpatterns = [
    path('activities/', ActivityListCreateView.as_view(), name='activity-list'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('activities/', activity_list),
]