from django.shortcuts import render, redirect
from .forms import AutorizeForm, RegisterForm








def registration(request):
    form = RegisterForm()
    return render(request, 'app/register.html', context={'form': form})


def autorize(request):
    if request.method == 'POST':
        form = AutorizeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return redirect('successAutorize')
        else:
            return redirect('registration')
    form = AutorizeForm()
    return render(request, 'app/autorize.html', context={'form': form})


def successRegistration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return render(request, 'app/successRegistration.html', context={'name': name, 'email': email, 'password': password})
        return redirect('/app/registration')
    else:
        return redirect('/app/registration')




def successAutorize(request):
    return render(request, 'app/successAutorize.html')

