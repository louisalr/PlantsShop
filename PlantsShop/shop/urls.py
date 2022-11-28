from django.urls import path

#import all functions defined
from . import views
from .views import product_detail

app_name= 'shop'
urlpatterns = [
    #ex : /
    path('', views.IndexView.as_view(), name='home'),
    #ex : /product/sneaker
    path('product/<str:slug>/', product_detail, name="detail"),
    #ex : /add_to_cart/<item>
    path('add_to_cart/<int:article_id>', views.add_to_cart, name='add_to_cart')
]