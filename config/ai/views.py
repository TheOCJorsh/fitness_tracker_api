from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .utils import generate_workout_insight


class WorkoutInsightView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        insight = generate_workout_insight(request.user)

        return Response({
            "insight": insight
        })