from django.db import models
from accounts.models import BaseModel
from django.utils.timezone import now

# Create your models here.


# class Transection(BaseModel):
#     unique_id = models.CharField(max_length=10, null=True, blank=True, editable=False)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
#     referred_by_customer = models.ForeignKey(Customer, related_name='referred_by_customer',on_delete=models.CASCADE, null=True, blank=True) # noqa
#     amount = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
#     transection_type = models.CharField(max_length=10,  default='None',null=True)
#     description = models.TextField()
#     # lastTransectionID = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

#     def __str__(self) -> str:
#         return str(self.amount)

class ProductCategory(BaseModel):
    name = models.CharField(max_length=20, null=True, blank=True, editable=False)
    status = models.BooleanField(default=True)

class ProductUnit(BaseModel):
    name = models.CharField(max_length=20, null=True, blank=True, editable=False)
    status = models.BooleanField(default=True)

