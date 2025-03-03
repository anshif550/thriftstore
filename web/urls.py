from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("single_product/<int:id>/", views.single_product, name="single_product"),
    path('all-products/', views.all_products, name='all_products'),
    path('category/<int:id>/', views.category_products, name='category_products'),
] 
 