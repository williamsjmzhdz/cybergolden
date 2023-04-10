
import time
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.test import TestCase, Client
from django.contrib.auth.models import User

from .models import Employee, Customer
from .forms import AuthForm
from .views import login_page, logout_page



############################################# TESTS FOR MODELS #############################################
class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear un usuario para el empleado
        testuser = User.objects.create_user(username='testuser', password='testpass')
        testuser.save()
        
        # Crear un empleado para los tests
        test_employee = Employee.objects.create(
            user=testuser,
            position='CEO',
            phone_number='555-5555'
        )
        test_employee.save()
        
    def test_employee_str(self):
        employee = Employee.objects.get(id=1)
        expected_str = f'{employee.user.first_name} {employee.user.last_name} - {employee.position}'
        self.assertEqual(str(employee), expected_str)
        
    def test_employee_user_relationship(self):
        employee = Employee.objects.get(id=1)
        user = User.objects.get(id=1)
        self.assertEqual(employee.user, user)
        
    def test_employee_position_choices(self):
        # Testear que las opciones para el campo "position" son correctas
        employee = Employee.objects.get(id=1)
        position_choices = [choice[0] for choice in employee.POSITIONS]
        expected_choices = ['CEO', 'COO', 'SA', 'MO']
        self.assertEqual(position_choices, expected_choices)
        
    def test_employee_phone_number_field(self):
        # Testear que el campo "phone_number" admite un número telefónico válido
        employee = Employee.objects.get(id=1)
        phone_number = '123-4567'
        employee.phone_number = phone_number
        employee.save()
        self.assertEqual(employee.phone_number, phone_number)

class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for the customer
        cls.user = User.objects.create_user(
            username='customer_test_user',
            password='password123',
            first_name='Jane',
            last_name='Doe'
        )
        # Create a customer object
        cls.customer = Customer.objects.create(
            user=cls.user,
            wholesale_gentleman_suit_price=150.00,
            wholesale_youth_suit_price=100.00,
            wholesale_child_suit_price=75.00
        )

    def test_customer_str_method(self):
        self.assertEqual(str(self.customer), 'Jane Doe')

    def test_customer_created_at_auto_now_add(self):
        self.assertIsNotNone(self.customer.created_at)

    def test_customer_updated_at_auto_now(self):
        time.sleep(2)
        old_updated_at = self.customer.updated_at
        self.customer.wholesale_gentleman_suit_price = 175.00
        self.customer.save()
        self.assertNotEqual(self.customer.updated_at, old_updated_at)


############################################# TESTS FOR FORMS #############################################
class AuthFormTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

    def test_auth_form_valid(self):
        form_data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        form = AuthForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_auth_form_invalid(self):
        form_data = {
            'username': 'testuser',
            'password': 'wrongpass'
        }
        form = AuthForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_auth_form_missing_fields(self):
        form_data = {}
        form = AuthForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertIn('password', form.errors.keys())



############################################# TESTS FOR VIEWS #############################################
class LoginLogoutTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login_page_view_with_get(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertTrue(isinstance(response.context['form'], AuthForm))

    def test_login_page_view_with_post_and_valid_credentials(self):
        response = self.client.post(reverse('users:login'), data={
            'username': 'testuser',
            'password': '12345'
        })
        self.assertRedirects(response, reverse('users:profile'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_page_view_with_post_and_invalid_credentials(self):
        response = self.client.post(reverse('users:login'), data={
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertTrue(isinstance(response.context['form'], AuthForm))
        self.assertContains(response, 'Las credenciales son inválidas.')

    def test_logout_page_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('users:logout'))
        self.assertRedirects(response, reverse('users:login'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

class UpdateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        self.employee = Employee.objects.create(
            user=self.user,
            position='CEO',
            phone_number='5555555555'
        )
        self.client.login(username='testuser', password='testpass')

    def test_update_username(self):
        url = reverse('users:update')
        data = {
            'username': 'newusername',
            'email': '',
            'phone_number': '',
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(response.json()['message'], 'Usuario actualizado con éxito.')
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'newusername')

    def test_update_email(self):
        url = reverse('users:update')
        data = {
            'username': '',
            'email': 'newemail@example.com',
            'phone_number': '',
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(response.json()['message'], 'Usuario actualizado con éxito.')
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'newemail@example.com')

    def test_update_phone_number(self):
        url = reverse('users:update')
        data = {
            'username': '',
            'email': '',
            'phone_number': '5551234567',
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(response.json()['message'], 'Usuario actualizado con éxito.')
        self.user.employee.refresh_from_db()
        self.assertEqual(self.user.employee.phone_number, '5551234567')

    def test_invalid_username(self):
        url = reverse('users:update')
        data = {
            'username': 'new username with spaces',
            'email': '',
            'phone_number': '',
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')
        self.assertIn('El nombre de usuario debe contener entre 1 y 150 caracteres alfanuméricos, incluyendo los símbolos @ . + -', response.json()['message'])

    def test_invalid_email(self):
        url = reverse('users:update')
        data = {
            'username': '',
            'email': 'invalidemail',
            'phone_number': '',
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')
        self.assertIn('El correo electrónico ingresado no es válido.', response.json()['message'])

    def test_invalid_phone_number(self):
        url = reverse('users:update')
        data = {
            'username': '',
            'email': '',
            'phone_number': '1234',
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')
        self.assertIn('El número telefónico debe tener 10 dígitos', response.json()['message'])
