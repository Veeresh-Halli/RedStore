from django.urls import path
from . import views


urlpatterns=[

path('', views.index, name='index'),
path('products', views.products , name ='products'),
path('account', views.account , name ='account'),
path('productdetail/<int:id>/', views.productdetail, name ='productdetail'),
path('cart/', views.cart, name ='cart'),

path('update_item/', views.updateItem, name ='update_item'),

path('logout', views.logoutPage , name ='logout'),
path('login', views.loginPage , name ='login'),
]