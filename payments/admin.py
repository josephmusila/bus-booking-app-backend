from django.contrib import admin
from  . import models
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display=("id","amount","is_finished","is_successful","trans_id")


admin.site.register(models.PaymentTransaction,TransactionAdmin)