from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Регистрация успешна. Добро пожаловать, {user.username}!")
            return redirect('home')
        else:
            for error in form.errors:
                messages.error(request, f"{error}: {form.errors[error]}")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Добро пожаловать, {user.username}!")
                return redirect('home')
        else:
            messages.error(request, "Неправильное имя пользователя или пароль.")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы.")
    return redirect('home')

# Role-based access control decorators
def role_required(allowed_roles=[]):
    def decorator(view_func):
        @login_required
        def wrapped(request, *args, **kwargs):
            if hasattr(request.user, 'profile') and request.user.profile.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, "У вас нет прав для доступа к этой странице.")
                return redirect('home')
        return wrapped
    return decorator

# Example of a protected view for admins only
@role_required(['admin'])
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

# Example of a protected view for managers and admins
@role_required(['manager', 'admin'])
def manager_dashboard(request):
    return render(request, 'manager_dashboard.html')

# Example of a protected view for customers
@role_required(['customer', 'manager', 'admin'])
def customer_profile(request):
    return render(request, 'customer_profile.html')