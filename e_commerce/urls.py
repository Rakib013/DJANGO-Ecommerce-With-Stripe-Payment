from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "e_commerce"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('order-summary/', views.OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug:slug>/', views.ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('add-coupon/', views.AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug:slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug:slug>/', views.remove_single_item_from_cart, name="remove-single-item-from-cart"),
    path('payment/<payment_option>/', views.PaymentView.as_view(), name='payment'),
    path('request-refund/', views.RequestRefundView.as_view(), name='request-refund'),

    path('category/<str:category>/', views.ItemCategory.as_view(), name='item-category'),
    path('item/search/', views.ItemSearch.as_view(), name='item-search'),
    path('login/', views.MyLoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="e_commerce:home"), name="logout"),
    path('register/', views.UserRegister.as_view(), name="signup")
]
