from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Job
from .serializers import JobSerializer

class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

class JobListView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employer = self.request.user
        return Job.objects.filter(employer=employer)
