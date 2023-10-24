from django.urls import path
from  . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'sacco',views.SaccoView,basename='sacco')
router.register(r'routes',views.RouteView,basename="routes")
router.register(r'vehicles',views.VehicleView,basename='vehicles')
router.register(r'trips',views.TripView,basename="trips")
router.register(r'seats',views.SeatView,basename="seats")

urlpatterns=[
    path("sacco/routes/<pk>",views.AddSaccoRoutes.as_view(),name="sacco-routes"),
    path("vehicle/routes/<pk>",views.AddVehicleRoutes.as_view(),name="vehicle-routes"),
    path("bookseat/<int:pk>",views.UpdateSeatView.as_view(),name="book-seat")
]+router.urls

