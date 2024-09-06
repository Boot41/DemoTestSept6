from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employer, Job

class JobTests(APITestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='Test Employer', email='employer@test.com')
        self.client.force_authenticate(user=self.employer)

    def test_create_job(self):
        url = reverse('job-create')
        data = {'employer': self.employer.id, 'title': 'Software Engineer', 'description': 'Job Description'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 1)
        self.assertEqual(Job.objects.get().title, 'Software Engineer')

    def test_list_jobs(self):
        Job.objects.create(employer=self.employer, title='Software Engineer', description='Job Description')
        url = reverse('job-list', kwargs={'employer_id': self.employer.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
