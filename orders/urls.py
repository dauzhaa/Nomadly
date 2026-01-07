from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'orders'

router = DefaultRouter()

router.register(r'', views.OrderViewSet, basename='orders')
router.register(r'items', views.OrderItemsViewSet, basename='order-items')

urlpatterns = [
    path('', include(router.urls))
]
