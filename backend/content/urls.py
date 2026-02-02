from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'content'

router = DefaultRouter()

router.register(r'', views.ContentViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls))
]
    