from django.contrib.auth.decorators import login_required
from django.urls import path
from . import  views

urlpatterns = [
    path('identify/dataset/create/',login_required(views.CreateIdentifyDataSetView.as_view()),name=""),

]
