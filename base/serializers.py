from rest_framework import serializers
from . import models
from userauth.serializers import UserSerializer
from userauth.models import User


class RouteSerializer(serializers.ModelSerializer):
    # sacco=serializers.PrimaryKeyRelatedField(many=False,queryset=models.Sacco.objects.all())
    class Meta:
        model = models.Routes
        fields=('id','description','fare','start','destination')



class SaccoSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True,read_only=True)
    # vehicles=VehicleSerializer(many=True,read_only=True)
    class Meta:
        model = models.Sacco
        # fields=('id','name', 'description','vehicles')
        fields=('id','name', 'description','routes')
        depth=2

    def to_representation(self, instance):
          response = super().to_representation(instance)
        #   response['routes'] = RouteSerializer(instance.routes).data
          return response
    
    # def update(self, instance, validated_data):
    #     instance.sacco = validated_data["sacco"]
    #     instance.
    #     return super().update(instance, validated_data)


class VehicleSerializer(serializers.ModelSerializer):
    # routes=RouteSerializer(many=True,read_only=True,)
    sacco=serializers.PrimaryKeyRelatedField(many=False,queryset=models.Sacco.objects.all())
    class Meta:
        model=models.Vehicle
        fields=('id','capacity','registration','image','sacco')

    # def to_representation(self, instance):
    #       response = super().to_representation(instance)
    #       response['routes'] = RouteSerializer(instance.routes).data
    #       return response

# class SeatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=models.Seat
#         fields=("id","customer","seat_number","isBooked")


class SeatSerializer(serializers.ModelSerializer):
    # trip = serializers.PrimaryKeyRelatedField(many=False,queryset=models.Trip.objects.all())
    customer=serializers.PrimaryKeyRelatedField(many=False,queryset=User.objects.all())
    class Meta:
        model = models.Seat
        fields = ("id","seat_number","isBooked","customer",)
        
        # depth = 2


    def update(self, instance, validated_data):
        instance.customer = validated_data["customer"]
        instance.seat_number=validated_data["seat_number"]
        instance.isBooked = validated_data["isBooked"]
        return super().update(instance, validated_data)


    def to_representation(self, instance):
          response = super().to_representation(instance)
          response['customer'] = UserSerializer(instance.customer).data
          return response


class TripSerializer(serializers.ModelSerializer):
    vehicle=serializers.PrimaryKeyRelatedField(many=False,queryset=models.Vehicle.objects.all())
    routes=serializers.PrimaryKeyRelatedField(many=False,queryset=models.Routes.objects.all())
    # vehicle=VehicleSerializer(many=False,read_only=False)
    sacco=serializers.PrimaryKeyRelatedField(many=False,queryset=models.Sacco.objects.all())
    seats = SeatSerializer(many=True,read_only=True)

    class Meta:
        model = models.Trip
        # fields = ("id","vehicle","pickuppoint","date","sacco","seats"),
        fields = "__all__"
       
        depth=2


    

    # def update(self, instance, validated_data):
    #       instance_keyword=instance.keywords.copy()
    #       instance_keyword.update(validated_data.get("seats",[]))
    #       print(instance_keyword)
    #       validated_data["seats"]=instance_keyword
    #       return super().update(instance, validated_data)


     
    def to_representation(self, instance):
          response = super().to_representation(instance)
          response['sacco'] = SaccoSerializer(instance.sacco).data
          response['vehicle'] = VehicleSerializer(instance.vehicle).data
          response['routes'] = RouteSerializer(instance.routes).data
          return response