from django.shortcuts import get_object_or_404, render


def user_login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def dashboard(request):
    pass

def logout(request):
    pass
