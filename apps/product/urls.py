from django.urls import path

from apps.product import views
from apps.product.views import AddProduct, ProductListView, UpdateProductView, UserDeleteView, SignUp, LogIn,SignupListView

app_name = "product"

urlpatterns = [
    path('rahul',views.rahul),
    # path('product_list',views.product_list),
    path('add_product/', AddProduct.as_view(), name='add_product'),
    # path('product_list', ProductList.as_view()),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('UpdateProductView/<int:pk>/', UpdateProductView.as_view(), name='UpdateProductView'),
    path('UserDeleteView/<int:pk>/', UserDeleteView.as_view(), name='UserDeleteView'),
    # singup path
    path('signUp',SignUp.as_view(),name="signUp"),
    path('LogIn',LogIn.as_view(),name="LogIn"),
    path('signup_list', SignupListView.as_view(), name='signup_list'),

]
