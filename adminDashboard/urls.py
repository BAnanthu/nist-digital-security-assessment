from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', login_required(views.HomeView.as_view()), name="main"),
    path('main/<int:function_id>/<int:category_id>/<int:sub_category_id>/<str:direction>/<str:screen_type>/',login_required(views.HomeView.as_view()), name="home"),
]
