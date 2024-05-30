from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages # to show flash messages
from django.contrib.auth import authenticate, login, logout

from .forms import PackageForm, RegistrationForm, AddressForm
from .models import User, Address

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)


def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "Username not found")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Username or Password is incorrect")

    context = {'page': page}
    return render(request, 'login.html', context)

def userLogout(request):
    logout(request)
    return redirect("/")

def userRegister(request):
    page = 'register'
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'An error occured during registration! ')
        

    context = {'page': page, 'form': form}
    return render(request, 'login.html', context)

@login_required(login_url="/login") 
def send_package(request):
    form = PackageForm()
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Package registration successfull')
            return redirect('/')
    context = {'form': form}
    return render(request, 'send_package.html', context)

@login_required(login_url="/login")
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    user_addresses = Address.objects.filter(customer=user)
    context = {"user": user, "user_addresses": user_addresses}
    return render(request, 'profile.html', context)

@login_required(login_url="/login")
def edit_address(request, pk):
    address = Address.objects.get(id=pk)
    user = request.user
    if address.customer != user:
        return HttpResponse("You cannot edit this address")

    form = AddressForm(instance=address)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('/profile/'+ str(user.id))

    context = {'form': form}
    return render(request, 'editAddress.html', context)