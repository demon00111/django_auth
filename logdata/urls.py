from . import views
from django.urls import path

urlpatterns = [
    path('', views.signup , name='signup'),
    path('login/', views.loginpage , name='signup'),
    path('logpage/', views.logpage , name='logpage'),
    path('changepass/', views.changepass , name='changepass'),
]
