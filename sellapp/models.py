from django.db import models
from customerapp.models import *
from productapp.models import *
from accounts.models import BaseModel

# Create your models here.

class Order(BaseModel):
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    unique_id = models.CharField(max_length=5, null=True, blank=True, editable=False)
    subPrice = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    totalPrice = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    duePrice = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    vat = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    vatParcent = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    discount = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    discountParcent = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    transport = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    returnTime = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.unique_id)
    
class CustomerOrder(BaseModel):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE,null=True, blank=True)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    address = models.CharField(max_length=10, null=True, blank=True, editable=False)
    mobile_number = models.CharField(max_length=10, null=True, blank=True, editable=False)


class ProductOrder(BaseModel):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE,null=True, blank=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE,null=True, blank=True)
    sellPrice = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    unit = models.IntegerField(default=0.00)



