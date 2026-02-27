from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Activity, Milestone
from .serializers import ActivitySerializer, MilestoneSerializer
from django.db.models import Sum, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

class ActivityListCreateView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        activity = serializer.save(user=self.request.user)
        

class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)


class MilestoneListView(generics.ListAPIView):
    serializer_class = MilestoneSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Milestone.objects.filter(user=self.request.user)
    

class ActivityAnalyticsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        activities = Activity.objects.filter(user=request.user)

        if start_date and end_date:

            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

                activities = activities.filter(
                    activity_date__range=(start_date, end_date)
                )

            except ValueError:
                return Response(
                    {"error": "Invalid date format. Use YYYY-MM-DD"},
                    status=400
                )

        analytics = activities.aggregate(

            total_activities=Count('id'),

            total_distance=Sum('distance_km'),

            total_calories=Sum('calories_burned'),

            total_duration=Sum('duration_minutes')

        )

        # Replace None with 0
        analytics = {
            key: value or 0
            for key, value in analytics.items()
        }

        return Response(analytics)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def activity_list(request):

    if request.method == 'GET':
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)