from django.urls import path
from . import views

app_name = 'polls'  # Add this line

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URL patterns here as needed
]
