from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoModelTests(TestCase):

    def test_todo_creation(self):
        todo = Todo.objects.create(title="Test Todo", description="A test todo", completed=False)
        self.assertEqual(todo.title, "Test Todo")

    def test_todo_str_method(self):
        todo = Todo.objects.create(title="Test Todo", description="A test todo", completed=False)
        self.assertEqual(str(todo), "Test Todo")

class TodoViewTests(TestCase):

    def test_todo_list_view(self):
        Todo.objects.create(title="Test Todo", description="A test todo", completed=False)
        response = self.client.get(reverse('todo_list'))  # Ensure 'todo_list' matches the name in urls.py
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")
