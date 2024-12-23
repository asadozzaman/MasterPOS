from django.db import models
from category.models import *
# Create your models here.


class Product(BaseModel):
    unique_id = models.CharField(max_length=5, null=True, blank=True, editable=False)
    name = models.CharField(max_length=10, null=True, blank=True, editable=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,null=True, blank=True)
    unit = models.ForeignKey(ProductUnit, on_delete=models.CASCADE,null=True, blank=True)
    buyPrice = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    sellPrice = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    discount = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    stock = models.IntegerField(default=0.00)

    def __str__(self) -> str:
        return str(self.name)