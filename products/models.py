from django.db import models


# Sizes for suits and shirts
SIZES = [
    ("0", "0"),
    ("2", "2"),
    ("4", "4"),
    ("6", "6"),
    ("8", "8"),
    ("10", "10"),
    ("12", "12"),
    ("14", "14"),
    ("16", "16"),
    ("18", "18"),
    ("20", "20"),
    ("34", "34"),
    ("36", "36"),
    ("38", "38"),
    ("40", "40"),
    ("42", "42"),
    ("44", "44"),
    ("46", "46"),
    ("48", "48"),
    ("50", "50"),
]

# Sizes for age
SIZES_BY_AGE = [
    ("N", "NIÑO"),
    ("J", "JUVENIL"),
    ("J", "CABALLERO"),
]


class Category(models.Model):
    """
    Model that represents a category in the database.
    """
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model that represents a product in the database.
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    #available = models.BooleanField(default=True) <-- Va en la tabla ProductInventory
    production_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False) # Costo sin caballo
    logistics_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False) # Costo con caballo
    #stock = models.IntegerField(default=0, blank=True, null=True) # <-- Va en la tabla ProductInventory
    minimum_stock = models.IntegerField(blank=False, null=False)
    size = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name