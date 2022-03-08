from django.urls import path
from . import views

urlpatterns = [
    path('progress/', views.Progress.as_view(), name=""),
    path('data/', views.GetData.as_view(), name=""),
    path('functions/', views.FunctionView.as_view(), name=""),
    path('assessed-maturity-level/', views.AssessedMaturityLevelView.as_view(), name="assessed-maturity-level"),
    path('your-desired-level-view/', views.YourDesiredLevelView.as_view(), name="your-desired-level-view"),
]
