from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    pass
    return render(request, 'index.html')


def login(request):
    pass
    return render(request, 'signin.html')


def register(request):
    pass
    return render(request, 'signup.html')


def logout(request):
    pass
    return redirect("/login/")


def about(request):
    pass
    return render(request, 'about.html')


def services(request):
    pass
    return render(request, 'services.html')


def portfolio(request):
    pass
    return render(request, 'portfolio.html')


def contact(request):
    pass
    return render(request, 'contact.html')
