from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    '''
    Model that represents a user profile in the database
    '''

    POSITIONS = [
        ('CEO', 'Director ejecutivo'),
        ('COO', 'Director de operaciones'),
        ('SA', 'Agente de ventas'),
        ('MO', 'Operador de maquiladora'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, choices=POSITIONS, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.position}'
    
class Customer(models.Model):
    '''
    Model that represents a customer in the database
    ''' 

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wholesale_gentleman_suit_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    wholesale_youth_suit_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    wholesale_child_suit_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'