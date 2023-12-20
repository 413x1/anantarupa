from django.urls import path
from apps.views import Purchase


urlpatterns = [
    path("purchase/", Purchase.as_view(), name="purchase-item"),
]