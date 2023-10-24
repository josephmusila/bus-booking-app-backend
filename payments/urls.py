from .  import views
from django.urls import path

urlpatterns=[
    path('submit/', views.SubmitView.as_view(), name='submit'),
    path('confirm/', views.ConfirmView.as_view(), name='confirm'),
    path('check-online/', views.CheckTransactionOnline.as_view(), name='confirm-online'),
    path('check-transaction/', views.CheckTransaction.as_view(), name='check_transaction'),
]