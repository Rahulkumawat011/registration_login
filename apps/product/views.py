from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.product.ModelForm import ProductForm
from apps.product.models import Product, UserSignUp


# Create your views here.
def rahul(request):
    return HttpResponse("hiii")

# def product_list(request):
#     # Your view logic here
#     return render(request, 'product_list.html')


class AddProduct(CreateView):
    model=Product
    # fields = "__all__"
    # fields = ['first_name','last_name']
    form_class = ProductForm
    template_name = 'product_form.html'
    # success_url = reverse_lazy('create_user')
    success_url = '/product_list'

# class ProductList(ListView):
#     model = Product
#     template_name = "product_list.html"

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, "product_list.html", context={"products": products})


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"


class UpdateProductView(UpdateView):
    model=Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = '/product_list'


class UserDeleteView(DeleteView):
    model = Product
    success_url = '/product_list'
    template_name = 'delete_product.html'


class SignUp(CreateView):
    model = UserSignUp
    fields = '__all__'
    template_name = 'signUp.html'
    success_url = '/signup_list'


class LogIn(LoginView):
    template_name = 'login.html'
    fields = ['email','password']
    success_url = '/signup_login'

    def form_valid(self, form, request):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            LogIn(self.request, user)
            return render(request, template_name='signup_login.html')
        else:
            form.add_error(None, "Username or Password is Incorrect")
            return render(request, template_name='signUp.html')





class SignupListView(ListView):
    model = UserSignUp
    template_name = "signup_login.html"
    context_object_name = "signups"

    # def get(self,request):
    #     signups = UserSignUp.objects.all()
    #     return render(request, template_name=self.template_name, context={'signups':signups})






