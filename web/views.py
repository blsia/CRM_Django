
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout # <-- Pakai alias jika perlu
from django.contrib import messages 
from .forms import Register

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
            return redirect('home')
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
        if form.is_valid():  # <-- Tambahkan tanda kurung () di sini
            username = form.cleaned_data['username']
            # Perbaiki typo 'passsword1' -> 'password1'
            password = form.cleaned_data['password1'] 
            
            form.save()
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Berhasil bikin akun")
                return redirect('home')
        else:
            # Jika form tidak valid, kembalikan halaman register beserta pesan errornya
            return render(request, 'register.html', {'form': form})
    else:
        form = Register()

    return render(request, 'register.html', {'form': form})