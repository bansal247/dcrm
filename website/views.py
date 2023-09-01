from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()


    # Check tp see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have Been loggedIn")
            return redirect('home')
        else:
            messages.success(request, "Please try again")
            return redirect('home')
        
    else:
        return render(request,'home.html',{'records':records})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logout")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print(username,password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "You have been successfully registered")
                return redirect('home')
            else:
                messages.success(request, "Please try again")
                return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})



def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request, "User not authenticated")

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Customer deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "User not authenticated")

def add_record(request):
    if request.user.is_authenticated:
        form =  AddRecordForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                add_record  = form.save()
                messages.success(request, "Customer added successfully")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request, "User not authenticated")
        return redirect('home')

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form =  AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer has been updated")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request, "User not authenticated")
        return redirect('home')

