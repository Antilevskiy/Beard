from django.test import TestCase
from .models import Todo, User


class TodoTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(id=1, name='Ivan')
        Todo.objects.create(id=201, user_id=user1, title='Wash car', completed=False)
        Todo.objects.create(id=202, user_id=user1, title='Buy apples', completed=True)

    def test_todo(self):
        todo = Todo.objects.get(id=201)
        self.assertEqual(todo.title, 'Wash car')
        self.assertEqual(todo.completed, False)

    def test_amount(self):
        qs = Todo.objects.all()
        self.assertEqual(len(qs), 2)


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(id=1, name='Ivan')
        User.objects.create(id=2, name='Bogdan', city='Odessa')
        User.objects.create(id=3, name='Mike', company_name='PandaDoc')

    def test_user(self):
        user1 = User.objects.get(id=1)
        user2 = User.objects.get(id=2)
        user3 = User.objects.get(id=3)
        self.assertEqual(user1.name, 'Ivan')
        self.assertEqual(user1.city, '')
        self.assertEqual(user2.name, 'Bogdan')
        self.assertEqual(user2.city, 'Odessa')
        self.assertNotEqual(user3.name, 'mike')
        self.assertEqual(user3.company_name, 'PandaDoc')

    def test_amount(self):
        qs = User.objects.all()
        self.assertEqual(len(qs), 3)
