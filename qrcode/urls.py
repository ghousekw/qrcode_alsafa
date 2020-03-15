from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('emp', views.EmployessCreate.as_view(), name="index"),
]
