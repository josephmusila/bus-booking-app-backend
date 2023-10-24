from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'first_name','last_name', 'email', 'password','phone','idnumber','is_superuser']
     #    fields="__all__"

    # hide password
        extra_kwargs = {
            'password': {'write_only':True}
        }


    # hash passwords in the database, override default create function
    def create(self, validated_data):
        #extract password
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data) #doesnt include password

        if password is not None:
            instance.set_password(password) #hashes password
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
         print("update method called")
         instance.first_name=validated_data["first_name"]
         instance.last_name=validated_data["last_name"]
         instance.email=validated_data["email"]
         instance.phone=validated_data["phone"]
         instance.idnumber=validated_data["idnumber"]
         instance.set_password(validated_data["password"])
         print(instance.password)

         instance.save()
         return instance
    
