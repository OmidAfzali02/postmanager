from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages # to show flash messages
from django.contrib.auth import authenticate, login, logout

from .forms import PackageForm, RegistrationForm, AddressForm, AgentForm
from .models import User, Address, Agent, Package
from .qr import qr_encode

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
            instance = form.save(commit=False)
            instance.qr_code = qr_encode(instance, str(instance.id))
            instance.save()
            messages.success(request, 'Package registration successfull')
            return redirect('/')
    context = {'form': form}
    return render(request, 'send_package.html', context)

@login_required(login_url="/login") 
def track_package(request, pk):
    user = request.user
    package = Package.objects.filter(id=pk).first()
    sender = User.objects.filter(phone=package.sender_phone).first()
    reciever = User.objects.filter(phone=package.receiver_phone).first()

    if package is None:
        HttpResponse(request, f"Couldn't find any package with this id: {pk}")

    if package.sender_phone != user.phone or package.receiver_phone != user.phone:
        HttpResponse(request, "You do not have access to this page \nonly sender and reciever can track package")

    context = {'package': package, 'sender': sender, 'reciever':reciever}    
    return render(request, 'track.html', context)


@login_required(login_url="/login")
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    agencies = Agent.objects.filter(agent=user)
    user_addresses = Address.objects.filter(customer=user)
    sended_packages = Package.objects.filter(sender_phone=user.phone)
    recieved_packages = Package.objects.filter(receiver_phone=user.phone)
    context = {"user": user, "user_addresses": user_addresses, 'agencies':agencies, 'sended_packages':sended_packages, 'recieved_packages':recieved_packages}
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

@login_required(login_url="/login") 
def createAddress(request):
    user = request.user
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False) 
            instance.customer = user 
            instance.save()
            messages.success(request, "Address add successful")

            return redirect('/profile/'+str(user.id))
    context = {'form': form}
    return render(request, 'createAddress.html', context)

@login_required(login_url="/login") 
def deleteAddress(request, pk):
    user = request.user
    address = Address.objects.get(id=pk)
    if address.customer != user:
        return HttpResponse(request, 'You are not allowed to access this page')
    
    if request.method == 'POST':
        address.delete()
        messages.success(request, "Address delete successful")
        return redirect('/profile/'+str(user.id))
    context = {'obj': address}
    return render(request, 'deleteAddress.html', context)

@login_required(login_url="/login") 
def agentSetup(request):
    user = request.user
    form = AgentForm()
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False) 
            instance.agent = user 
            instance.save()
            agency_id = instance.id
            messages.success(request, f"Agency registration successful \nYou agency id: {agency_id}")

            return redirect('/profile/'+str(user.id))
    context = {'form': form}
    return render(request, 'agentSetup.html', context)

@login_required(login_url="/login")
def agentProfile(request, pk):
    agency = Agent.objects.get(id=pk)
    user = agency.agent
    context = {"agency": agency, 'user':user}
    return render(request, 'agentProfile.html', context)

@login_required(login_url="/login")
def agentLogin(request):
    user = request.user
    agency = Agent.objects.filter(agent=user).first()
    if agency is None:
        return render(request, 'agent_notfound.html')
    context = {"agency": agency, 'user':user}
    return render(request, 'agentProfile.html', context)
