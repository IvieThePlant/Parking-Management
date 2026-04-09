from django.urls import path
from . import views

urlpatterns = [

    # API endpoints
    path('sessions/create/', views.create_session),
    path('sessions/update/', views.end_session)
]