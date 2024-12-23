from django.db import models
from customerapp.models import *
from productapp.models import *
from sellapp.models import *
# Create your models here.




class Payment(BaseModel):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE,null=True, blank=True)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    type = models.CharField(max_length=20, null=True, blank=True, editable=False)

class RetailerPayment(BaseModel):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE,null=True, blank=True)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    type = models.CharField(max_length=20, null=True, blank=True, editable=False)
