from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from users.forms import AuthForm


def login_page(request):

    if request.user.is_authenticated:
        pass
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