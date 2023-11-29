from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('son/<int:id>/', BossAdminView.as_view()),
    path('get_pro/<int:pk>/', GetProductView.as_view()),
    path('add/', AddProduct.as_view()),
    path('delete/', DeleteUserView.as_view()),
    path('edit/', EditPasswordAdminView.as_view()),
    path('login_u/', LoginView.as_view()),
]