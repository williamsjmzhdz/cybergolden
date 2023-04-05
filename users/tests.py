from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', first_name='first name', last_name='last name', email='testuser@example.com', password='password')
        self.profile = Profile.objects.create(user=self.user, nickname='test', profit_percentage=0.10, position='Gerente de tienda')

    def test_profile_creation(self):
        '''
        Test that a profile is created correctly
        '''
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.nickname, 'test')
        self.assertEqual(self.profile.profit_percentage, 0.10)
        self.assertEqual(self.profile.position, 'Gerente de tienda')

    def test_profile_str(self):
        '''
        Test that the __str__ method returns the expected string representation
        '''
        expected_string = 'first name last name - Gerente de tienda'
        self.assertEqual(str(self.profile), expected_string)
