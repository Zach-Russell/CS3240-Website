from django.test import TestCase
from .models import User, UserManager, Schedule

#Create your tests here.
class BasicTestingTests(TestCase):
    '''
    These are simple tests that should always pass since they have nothing to do with the project itself. 
    If one of these were to fail then something is probably broken with our testing system.
    '''
    def test_False_is_False(self):
        self.assertFalse(False)

    def test_True_is_True(self):
        self.assertTrue(True)

    def test_one_plus_one_is_two(self):
        self.assertEqual(1 + 1, 2)
    
    def test_one_plus_one_is_not_three(self):
        self.assertNotEqual(1 + 1, 3)


class UserTests(TestCase):
    '''
    These are tests for the User model. Eventually once large enough they should be moved to their own test file.
    '''
    None

class UserManagerTests(TestCase):
    '''
    These are tests for the UserManager model. Eventually once large enough they should be moved to their own test file.
    '''
    # def setUp(self):
    #     #ser.objects.create_user(email="TestUser000@gmail.com",password="test000")
    #     #User.objects.create_user(email="TestUser123@gmail.com",password="test123")
    #     u_man = UserManager()
    #     UserManager.create_user(self, email="abc@gmail.com",password="abc123")
    #     #user = User.objects.create_user("abc@gmail.com", "abc")

    def test_create_superuser_instance(self):
        model = User
        admin_user = model.objects.create_superuser(email="foobar@user.com", password="123abc", type="tut")
        self.assertTrue(isinstance(admin_user, User))

    def test_create_user_instance(self):
        model = User
        user = model.objects._create_user(email="foobar@user.com", password="123abc", type="tut", is_staff=False, is_superuser=False)
        self.assertTrue(isinstance(user, User))

class ScheduleTests(TestCase):
    '''
    These are tests for the Schedule model. Eventually once large enough they should be moved to their own test file.
    '''
    None