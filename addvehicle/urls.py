from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.listdata),
    path('add/', views.adddata),
    path('delete/<int:id>/', views.deletedata, name="delete"),
    path('update/<int:id>/', views.updatedata, name="update"),
     path('detail/<int:id>/', views.detaildata, name="detail"),
]