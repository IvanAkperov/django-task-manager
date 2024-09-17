from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task


class TaskAPITest(TestCase):

    """установка значения"""

    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Test Task', 'description': 'This is a test task'}
        self.response = self.client.post('/api/tasks/', self.task_data, format='json')

    """создание задачи"""

    def test_create_task(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    """получение списка задач"""

    def test_get_task_list(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)

    """получение конкретной задачи"""

    def test_get_task_detail(self):
        task = Task.objects.get()
        response = self.client.get(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """обновление задачи"""

    def test_update_task(self):
        task = Task.objects.get()
        updated_data = {'title': 'Updated', 'completed': True}
        response = self.client.put(f'/api/tasks/{task.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, 'Updated')

    """удаление задачи"""

    def test_delete_task(self):
        task = Task.objects.get()
        response = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
