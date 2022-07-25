from django.shortcuts import render
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def product(request):
    return render(request,'product.html')

def cart(request):
    return render(request,'cart.html')




def signup(request):
    return render(request,"signup.html")    

def signin(request):
    return render(request,"signin.html")   


    