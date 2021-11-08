from django.shortcuts import render
from django.views import View
from .models import OrderPlaced, customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm

#def home(request):
 #return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        COFFEE = Product.objects.filter(category='C')
        TEA = Product.objects.filter(category='T')
        SNACKS = Product.objects.filter(category='S')
        BRUNCH = Product.objects.filter(category='B')
        return render(request, 'app/home.html', {'COFFEE':COFFEE, 'TEA':TEA, 'SNACKS':SNACKS, 'BRUNCH':BRUNCH})

#def product_detail(request):
 #return render(request, 'app/productdetail.html')

class ProductDetailView(View):
     def get(self, request, pk):
         product = Product.objects.get(pk=pk)
         return render(request, 'app/productdetail.html', {'product':product})



def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def login(request):
 return render(request, 'app/login.html')

#def customerregistration(request):
 #return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self, request):
     form = CustomerRegistrationForm()
     return render(request, 'app/customerregistration.html',
     {'form':form})
     
    def post(self, request):
     form = CustomerRegistrationForm(request.POST)
     if form.is_valid():
      form.save()
     return render(request, 'app/customerregistration.html',
     {'form':form})


def checkout(request):
 return render(request, 'app/checkout.html')
