from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from users.forms import AuthForm
from users.models import Employee


def login_page(request):

    if request.user.is_authenticated:
        return redirect('users:profile')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('users:profile')
        else:
            return render(request, 'users/login.html', {
                'form': AuthForm(request.POST),
                'error': 'Las credenciales son inválidas.'
            })

    return render(request, 'users/login.html', {
        'form': AuthForm(),
    })

@login_required
def logout_page(request):
        
	logout(request)
	return redirect('users:login')

# Faltan tests
@login_required
def profile(request):
    try:
        employee = request.user.employee
        see_sales = employee.position in ['SA', 'CEO', 'COO']
    except Employee.DoesNotExist:
        employee = None
        see_sales = False

    print(employee, see_sales)
    context = {'employee': employee, 'see_sales': see_sales}
    
    return render(request, 'users/profile.html', context)
