from django.urls import path
from .views import WorkoutInsightView

urlpatterns = [

    path('workout-insights/',WorkoutInsightView.as_view()),

]