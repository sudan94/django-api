from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15, default=99.99)
    active = models.BooleanField(default=True)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        return "A discount of 20%"

