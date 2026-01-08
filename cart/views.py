from rest_framework import viewsets
from cart.serializers import CartSerializer
from cart.models import Cart
class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            
        key = self.request.session.session_key
        
        return Cart.objects.filter(session_key=key)

    def perform_create(self, serializer):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            
        key = self.request.session.session_key
        serializer.save(session_key=key)