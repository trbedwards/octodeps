from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from jobs.views import home_page
from jobs.models import Job

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

class JobModelTest(TestCase):

    def test_saving_and_retrieving_jobs(self):
        first_job = Job()
        first_job.name = 'first_job_ever'
        first_job.save()

        second_job = Job()
        second_job.name = 'job_number_two'
        second_job.save()

        saved_jobs = Job.objects.all()
        self.assertEqual(saved_jobs.count(), 2)

        first_saved_job = saved_jobs[0]
        second_saved_job = saved_jobs[1]

        self.assertEqual(first_saved_job.name, 'first_job_ever')
        self.assertEqual(second_saved_job.name, 'job_number_two')
