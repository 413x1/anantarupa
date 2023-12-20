from .serializers import PurchaseSerializer
from rest_framework import generics


class Purchase(generics.CreateAPIView):
    serializer_class = PurchaseSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



