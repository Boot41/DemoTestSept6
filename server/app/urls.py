from django.urls import path
from .views import JobCreateView, JobListView

urlpatterns = [
    path('jobs/', JobCreateView.as_view(), name='job-create'),
    path('employers/<int:employer_id>/jobs/', JobListView.as_view(), name='job-list'),
]
