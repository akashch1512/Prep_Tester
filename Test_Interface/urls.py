from django.urls import path
from . import views

urlpatterns = [
    path('', views.mcq_test, name='Test'),  # root URL shows your app's home view
]
