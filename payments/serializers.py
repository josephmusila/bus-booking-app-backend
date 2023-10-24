from rest_framework import serializers
from .payment_validators import validate_possible_number

from . import models
from  django.core.exceptions import ValidationError



class MpesaCheckOutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.PaymentTransaction
        fields=(
            "phone_number",
            "amount",
            "reference",
            "description"
        )


    def validate_phone_number(self,phone_number):
        if phone_number[0] == "+":
            phone_number=phone_number[1:]
        if phone_number[0] == "0":
            phone_number = "254" + phone_number[1:]

        try:
            validate_possible_number(phone_number,"KE")

        except ValidationError:
            raise serializers.ValidationError({
                "error":"Phone Number is Valid"
            })
        
        return phone_number
    

    def validate_amount(self,amount):
        if not amount or float(amount) <= 0:
            raise serializers.ValidationError({
                "error":"Amount must be greater than zero"
            })
        
        return amount
    
    def validate_reference(self,reference):
        if reference:
            return reference
        
        return "Test"
    
    def validate_description(self,description):
        if description:
            return description
        return "Test"
    
class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.PaymentTransaction
        fields="__all__"