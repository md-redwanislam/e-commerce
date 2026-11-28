from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
  path('register/', views.register_view),
  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('products/', views.get_products),
  path('products/<int:pk>/', views.get_product),
  path('categories/', views.get_categories),
  path('cart/', views.get_cart, name='get_cart'),
  path('cart/add/', views.add_to_cart, name='add_to_cart'),
  path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
  path('cart/update/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
  path('orders/', views.create_order),
]