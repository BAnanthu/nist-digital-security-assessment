from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.SignIn.as_view(), name="login"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('signout/', views.signout, name="signout"),
]
