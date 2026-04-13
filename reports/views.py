from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def home(request):
    context = {
        'location': 'Mahikeng',
        'fault_count': 2,
        'recent_updates': [
            {'id': 1023, 'status': 'Resolved', 'area': 'Montshiwa Street'},
            {'id': 1019, 'status': 'In progress', 'area': 'Unit 7'},
        ]
    }
    return render(request, 'reports/home.html', context)

def report_fault(request):
    return render(request, 'reports/report_fault.html')

def track_fault(request):
    return render(request, 'reports/track_fault.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'reports/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'reports/login.html', {'form': form})

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')


