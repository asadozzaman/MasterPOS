from django.db import models
from accounts.models import *
from productapp.models import *
from accounts.models import BaseModel

# Create your models here.



class Retailer(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    unique_id = models.CharField(max_length=5, null=True, blank=True, editable=False)
    totalSpent = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    due = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)



class ROrder(BaseModel):
    retailerID = models.ForeignKey(Retailer, on_delete=models.CASCADE,null=True, blank=True)
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
    
class RetailerOrder(BaseModel):
    orderID = models.ForeignKey(ROrder, on_delete=models.CASCADE,null=True, blank=True)
    retailerID = models.ForeignKey(Retailer, on_delete=models.CASCADE,null=True, blank=True)
    address = models.CharField(max_length=10, null=True, blank=True, editable=False)
    mobile_number = models.CharField(max_length=10, null=True, blank=True, editable=False)


class ProductROrder(BaseModel):
    orderID = models.ForeignKey(ROrder, on_delete=models.CASCADE,null=True, blank=True)
    productID = models.ForeignKey(Product, related_name='shop_product_orders',on_delete=models.CASCADE,null=True, blank=True)
    sellPrice = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    unit = models.IntegerField(default=0.00)


class RetailerPayment(BaseModel):
    orderID = models.ForeignKey(ROrder, on_delete=models.CASCADE,null=True, blank=True)
    customerID = models.ForeignKey(Retailer, on_delete=models.CASCADE,null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    type = models.CharField(max_length=20, null=True, blank=True, editable=False)
