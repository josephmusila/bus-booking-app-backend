from django.shortcuts import render
from rest_framework import views,viewsets,generics
from . import models,serializers
from rest_framework.response import Response
from .models import Seat
from  userauth.models import User
# Create your views here.


class SaccoView(viewsets.ModelViewSet):
    queryset=models.Sacco.objects.all()
    serializer_class=serializers.SaccoSerializer
    allowed_methods=["POST","GET","PUT","PATCH","DELETE"]



class RouteView(viewsets.ModelViewSet):
    queryset=models.Routes.objects.all()
    serializer_class=serializers.RouteSerializer
    allowed_methods=["POST","GET","PUT","PATCH","DELETE"]    

class AddSaccoRoutes(generics.UpdateAPIView):
    serializer_class = serializers.SaccoSerializer
    queryset = models.Sacco.objects.all()

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        # request.data._mutable=True
        routes_data=request.data.pop("routes")
        print(routes_data)
        serializer=self.get_serializer(instance,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        sacco=serializer.save()
        routes_instance=models.Routes.objects.get(id=routes_data)
        sacco.routes.add(routes_instance)
        # print(routes_data)
        return Response(serializer.data,)

class VehicleView(viewsets.ModelViewSet):
    queryset=models.Vehicle.objects.all()
    serializer_class=serializers.VehicleSerializer
    allowed_methods=["POST","GET","PUT","PATCH","DELETE"] 


    def get_queryset(self):
        id=self.request.query_params.get('id',None)
        queryset=models.Vehicle.objects.filter(sacco__id=id)
        # print(queryset.count())
        return queryset


class AddVehicleRoutes(generics.UpdateAPIView):
    serializer_class = serializers.VehicleSerializer
    queryset = models.Vehicle.objects.all()

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        # request.data._mutable=True
        routes_data=request.data.pop("routes")
        print(routes_data)
        serializer=self.get_serializer(instance,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        vehicle=serializer.save()
        routes_instance=models.Routes.objects.get(id=routes_data)
        vehicle.routes.add(routes_instance)
        # print(routes_data)
        return Response(serializer.data,)

class TripView(viewsets.ModelViewSet):
    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer
    # parser_classes = [MultiPartParser,FormParser]
    # allowed_methods = ["POST","GET","PUT","PATCH","DELETE"] 



    def create(self, request, *args, **kwargs):
        seats_data=request.data.pop('seats',[])
        # routes_data=request.data.pop("routes",[])
        trip_serializer=serializers.TripSerializer(data=request.data)

        if trip_serializer.is_valid():
            trip=trip_serializer.save()

            for seat in seats_data:
                seat_serializer=serializers.SeatSerializer(data=seat)
                if seat_serializer.is_valid():
                    seat=seat_serializer.save()
                    trip.seats.add(seat)
                else:
                    return Response(seat_serializer.errors)
                
            # for route in routes_data:
            #     route_serializer = serializers.RouteSerializer(data=route)
            #     if(route_serializer.is_valid):
            #         route=route_serializer.save()
            #         trip.routes.add(route)


            return Response(trip_serializer.data)
        return Response(trip_serializer.errors)
        # return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        seats=kwargs.pop('seats',False)
        print(seats)
        instance=self.get_object()
        serializer = self.get_serializer(instance,data=request.data,partial=seats)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializers.SeatSerializer(instance.parent).data)

        
class SeatView(viewsets.ModelViewSet):
    queryset = models.Seat.objects.all()
    serializer_class = serializers.SeatSerializer


    def get_object(self,obj_id):
        try:
            return models.Seat.objects.get(id=obj_id)
        except (models.Seat.DoesNotExist):
            return Response({"message":"Seat Does not Exist"})
        return True


    def validate_ids(self,id_lists):
        for id in id_lists:
            try:
                models.Seat.objects.get(id=id)

            except(models.Seat.DoesNotExist):
                return Response({"message":"Seat Does Not Exist"})
            
        return True



    def put(self,request,*args,**kwargs):
        data=request.data
        print(data)

        seat_ids=[i["id"] for i in data]
        self.validate_ids(seat_ids)
        instances=[]


        for seat in data:
            id=seat["id"]
            customer=seat["customer"]
            seat = self.get_object(obj_id=id)
            seat.isBooked=True
            seat.customer=User.objects.get(id=customer)
            seat.save()
            instances.append(seat)

        serializer = serializers.SeatSerializer(instances,many=True)
        return Response(serializer.data)


# class UpDateSeatsData(views.APIView):
#     def put()


class UpdateSeatView(generics.UpdateAPIView):
    queryset=models.Seat.objects.all()
    serializer_class=serializers.SeatSerializer






    

class UpDateTrip(generics.UpdateAPIView):
    queryset=models.Trip.objects.all()
    serializer_class = serializers.TripSerializer


class AddSeatsToTrip(generics.UpdateAPIView):
    queryset=models.Trip.objects.all()
    serializer_class=serializers.TripSerializer

    def partial_update(self, request, *args, **kwargs):
        instance  = self.get_object()
        seats_data=request.data.pop("seats")
        print(seats_data)
        serializer= self.get_serializer(instance,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        trip=serializer.save()
        seats_instance = models.Seat.objects.create(**seats_data)
        trip.seats.add(seats_instance)

        return Response(serializer.data)
        # return super().partial_update(request, *args, **kwargs)


class AddSeats(generics.ListAPIView):
    serializer_class=serializers.SeatSerializer
    allowed_methods=["POST"]
    queryset = models.Seat.objects.all()


    def post(self,request,format=None):
        serializer=serializers.SeatSerializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class GetSeats(views.APIView):
    def get(self,request):
        seats = models.Seat.objects.all()
        serializer = serializers.SeatSerializer(seats,many=True)
        return Response(serializer.data)
        # trips = 

class UpdateTripSeats(generics.UpdateAPIView):
    queryset=models.Trip.objects.all()
    serializer_class=serializers.TripSerializer