from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
    Model that represents a user profile in the database
    '''

    POSITIONS = [
        ('Gerente de tienda', 'Gerente de tienda'),
        ('Gerente de taller', 'Gerente de taller'),
        ('Gerente de venta', 'Gerente de venta'),
        ('Gerente general (CEO)', 'Gerente general (CEO)'),
        ('Ejecutivo de ventas', 'Ejecutivo de ventas'),
        ('Encargado de producción', 'Encargado de producción'),
        ('Encargado de corte', 'Encargado de corte'),
        ('Producción saco', 'Producción saco'),
        ('Producción pantalón', 'Producción pantalón'),
        ('Producción chaleco', 'Producción chaleco'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=False, blank=False)
    nickname = models.CharField(max_length=15, null=True, blank=True)
    profit_percentage = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    position = models.CharField(max_length=50, choices=POSITIONS, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.position}'