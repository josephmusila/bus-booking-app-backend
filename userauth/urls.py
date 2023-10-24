from django.urls import path
from . import views


urlpatterns=[
    path('register/', views.registerAPIView.as_view(),name="register"),
    path('login/', views.LoginAPIView.as_view(),name="login"),
    path('user/',views. UserView.as_view(),name="user"),
    path('logout/', views.LogoutView.as_view(),name="logout"),
    path('update_profile/<int:pk>/',views.UpdateProfileView.as_view(),name="update-profile"),

]