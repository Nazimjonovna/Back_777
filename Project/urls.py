from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegister.as_view()),
]