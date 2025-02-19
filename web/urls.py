from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("single_product/<int:id>/", views.single_product, name="single_product"),
] 
 