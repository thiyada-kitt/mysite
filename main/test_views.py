from django.test import TestCase, Client
from django.urls import reverse


class LandingPageTests(TestCase):
    """Test cases for the DevOps roadmap landing page"""
    
    def setUp(self):
        self.client = Client()
        self.url = reverse('landing_page')
    
    def test_landing_page_loads(self):
        """Test that the landing page loads successfully"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_landing_page_contains_devops(self):
        """Test that the landing page contains DevOps content"""
        response = self.client.get(self.url)
        self.assertContains(response, 'DEVOPS ROADMAP')
        self.assertContains(response, 'DevOps Roadmap')
    
    def test_landing_page_contains_levels(self):
        """Test that the landing page contains all learning levels"""
        response = self.client.get(self.url)
        self.assertContains(response, 'Foundations')
        self.assertContains(response, 'Intermediate')
        self.assertContains(response, 'Advanced')
    
    def test_landing_page_contains_technologies(self):
        """Test that the landing page contains key DevOps technologies"""
        response = self.client.get(self.url)
        self.assertContains(response, 'Docker')
        self.assertContains(response, 'Kubernetes')
        self.assertContains(response, 'CI/CD')
    
    def test_landing_page_template_used(self):
        """Test that the correct template is used"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'main/landing.html')