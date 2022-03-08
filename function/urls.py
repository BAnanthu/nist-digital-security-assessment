from django.urls import path
from . import views

urlpatterns = [
    path('identify/create/', views.CreateIdentifyByCategoryView.as_view(), name="identify_create"),
    path('identify/create/<int:pk>', views.CreateIdentifyByCategoryView.as_view(), name="identify_create"),


]
