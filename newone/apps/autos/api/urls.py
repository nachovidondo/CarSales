
from django.contrib import admin
from django.urls import path
from apps.autos.api.views.auto_views import CarListCreateAPIVIew,CarRetrieveAPIView,CarDestroyAPIView,CarUpdateAPIView

urlpatterns = [
    path('listados/',CarListCreateAPIVIew.as_view(),name ="listados"),
    path('detalle/<int:pk>/',CarRetrieveAPIView.as_view(),name ="detalle"),
    path('delete/<int:pk>/',CarDestroyAPIView.as_view(),name ="delete"),
    path('update/<int:pk>/',CarUpdateAPIView.as_view(),name="editar")
    
]
