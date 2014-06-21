from unittest import TestCase

from moat import Moat, Permission, ResourceMixin, UserMixin
from moat.repository import MockRepository


class Post(ResourceMixin):

    def __init__(self, id):
        self.id = id

    def type(self):
        return 'post'

    def identifier(self):
        return self.id


class User(UserMixin):

    def identifier(self):
        return 1

post1 = Post(1)
post2 = Post(2)
user = User()


class MoatTest(TestCase):

    def setUp(self):
        self.moat = Moat(MockRepository())

    def test_has(self):
        self.assertTrue(self.moat.has(Permission.read, user, post1))
        self.assertFalse(self.moat.has(Permission.write, user, post1))

    def test_set(self):
        self.assertFalse(self.moat.has(Permission.write, user, post1))
        self.assertTrue(self.moat.set(Permission.write, user, post1))
        self.assertTrue(self.moat.has(Permission.read, user, post1))

    def test_remove(self):
        self.assertTrue(self.moat.has(Permission.read, user, post1))
        self.assertTrue(self.moat.remove(Permission.read, user, post1))
        self.assertFalse(self.moat.remove(Permission.read, user, post1))
        self.assertFalse(self.moat.has(Permission.read, user, post1))

    def test_all(self):
        self.assertEquals(self.moat.all(Permission.read, user, Post), [1, 2])
