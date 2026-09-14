
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import Register, RecordForm
from .models import Record

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('records_list')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')

    return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"you have been logout.......")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] 
            
            form.save()
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Berhasil bikin akun")
                return redirect('records_list')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = Register()

    return render(request, 'register.html', {'form': form})

@login_required
def records_list(request):
    records = Record.objects.all().order_by('-created_at')
    return render(request, 'records_list.html', {'records': records})

@login_required
def record_add(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully!")
            return redirect('records_list')
    else:
        form = RecordForm()
    return render(request, 'record_form.html', {'form': form, 'action': 'Add'})

@login_required
def record_edit(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('records_list')
    else:
        form = RecordForm(instance=record)
    return render(request, 'record_form.html', {'form': form, 'action': 'Edit'})

@login_required
def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('records_list')
    return render(request, 'record_delete.html', {'record': record})

@login_required
def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'record_detail.html', {'record': record})