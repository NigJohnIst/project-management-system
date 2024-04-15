from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.utils.text import slugify
from .models import Project, Task
from .forms import TaskRegistrationForm, ProjectRegistrationForm
from register.models import Company
from django.contrib.auth.models import User

class ProjectTaskTestCase(TestCase):
    def setUp(self):
        # Create test data, for example, a company, users, and projects
        self.company = Company.objects.create(name="BrandArt")
        self.user1 = User.objects.create(username="user1")
        self.user2 = User.objects.create(username="user2")

    def test_task_registration_form(self):
        project = Project.objects.create(
            name="Test Project",
            slug="test-project",
            assign=self.user1,
            efforts=10,
            status='2',
            dead_line='2024-02-28',
            company=self.company,
            complete_per=0,
            description="Test project description",
        )

        data = {
            'project': project.id,
            'assign': [self.user1.id, self.user2.id],
            'task_name': 'Test Task',
            'status': '2',
            'due': '1',
        }

        form = TaskRegistrationForm(data)
        self.assertTrue(form.is_valid())

        task = form.save()

        self.assertEqual(task.project, project)
        self.assertEqual(task.assign.count(), 2)
        self.assertEqual(task.task_name, 'Test Task')
        self.assertEqual(task.status, '2')
        self.assertEqual(task.due, '1')

    def test_project_registration_form(self):
        data = {
            'name': 'Test Project',
            'slug': 'test-project',
            'assign': [self.user1.id, self.user2.id],
            'efforts': 10,
            'status': '1',
            'dead_line': '2024-02-28',
            'company': self.company.id,
            'complete_per': 0,
            'description': 'Test project description',
        }

        form = ProjectRegistrationForm(data)
        self.assertTrue(form.is_valid())

        project = form.save()

        self.assertEqual(project.name, 'Test Project')
        self.assertEqual(project.slug, 'test-project')
        self.assertEqual(project.assign.count(), 2)
        self.assertEqual(project.efforts, 10)
        self.assertEqual(project.status, '1')
        self.assertEqual(project.dead_line.strftime('%Y-%m-%d'), '2024-02-28')
        self.assertEqual(project.company, self.company)
        self.assertEqual(project.complete_per, 0)
        self.assertEqual(project.description, 'Test project description')

        # Additional test cases for Project model
        self.assertIsNotNone(project.add_date)
        self.assertIsNotNone(project.upd_date)
        self.assertTrue(project.add_date <= project.upd_date)

    def test_project_str_method(self):
        project = Project.objects.create(
            name="Test Project",
            slug="test-project",
            assign=self.user1,
            efforts=10,
            status='1',
            dead_line='2024-02-28',
            company=self.company,
            complete_per=0,
            description="Test project description",
        )
        self.assertEqual(str(project), 'Test Project')

    def test_task_str_method(self):
        project = Project.objects.create(
            name="Test Project",
            slug="test-project",
            assign=self.user1,
            efforts=10,
            status='1',
            dead_line='2024-02-28',
            company=self.company,
            complete_per=0,
            description="Test project description",
        )
        task = Task.objects.create(
            project=project,
            assign=self.user1,
            task_name='Test Task',
            status='2',
            due='1',
        )
        self.assertEqual(str(task), 'Test Task')
