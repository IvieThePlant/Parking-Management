from django.urls import path
from . import views

urlpatterns = [

    # API endpoints
    path('sessions/create/', views.createSession),
    path('sessions/update/', views.updateSessionStatus)
]