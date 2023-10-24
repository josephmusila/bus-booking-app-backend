from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField

STATUS = ((1,"pending"),(2,"Complete"))
# Create your models here.

class PaymentTransaction(models.Model):
    phone_number = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    is_finished = models.BooleanField(default=False)
    is_successful = models.BooleanField(default=False)
    trans_id = models.CharField(max_length=30)
    # bike=models.CharField(max_length=5,null=True,blank=True)
    order_id = models.CharField(max_length=200)
    checkout_request_id = models.CharField(max_length=100)
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    # content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.SET_NULL)
    # object_id = models.PositiveIntegerField(default=0)
    # content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "{} {}".format(self.phone_number, self.amount)


class Wallet(models.Model):
    phone_number = models.CharField(max_length=30)
    available_balance = models.DecimalField(('available_balance'), max_digits=6, decimal_places=2, default=0)
    actual_balance = models.DecimalField(('actual_balance'), max_digits=6, decimal_places=2, default=0)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.phone_number