"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from models import Server
from django.core.exceptions import ObjectDoesNotExist


class DatabaseTest(TestCase):
    '''
    Executes some basic test cases on Server model
    '''

    def setUp(self):
        Server.objects.create(name='test1', latitute=0, longitude=0)
        self.test1 = Server.objects.get(name='test1')

    def test_Create(self):
        self.assertEqual(self.test1.name, 'test1', 'Name doesnt match')

    def test_Delete(self):
        self.test1.delete()
        self.assertRaises(ObjectDoesNotExist, Server.objects.get, name='test1')



