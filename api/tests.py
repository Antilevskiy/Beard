from django.test import TestCase
from .models import Todo, User


class TodoTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(id=1, name='Ivan')
        Todo.objects.create(id=201, user_id=user, title='Wash car', completed=False)

    def test_todo(self):
        todo = Todo.objects.get(id=201)
        self.assertEqual(todo.title, 'Wash car')
        self.assertEqual(todo.completed, False)
