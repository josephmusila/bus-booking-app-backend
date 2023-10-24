from django.contrib import admin
from . import models
# Register your models here.


class TripAdmin(admin.ModelAdmin):
    list_display = ("id","pickuppoint",)



class VehicleAdmin(admin.ModelAdmin):
    list_display = ("id","registration","capacity")



admin.site.register(models.Trip,TripAdmin)
admin.site.register(models.Seat),
admin.site.register(models.Vehicle,VehicleAdmin)