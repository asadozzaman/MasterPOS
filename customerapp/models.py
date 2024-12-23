from django.db import models
from accounts.models import *
from productapp.models import *
from django.core.validators import RegexValidator

# Create your models here.



class Customer(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    unique_id = models.CharField(max_length=5, null=True, blank=True, editable=False)
    totalSpent = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    due = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)

