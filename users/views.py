from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import NewUserForm

# Create your views here.


def login_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect!')
    return render(request, 'login.html')

def logout_auth(request):
    logout(request)
    return redirect('homepage')

def register(request):
    return HttpResponse("Hello, world. You're at the register index.")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request)
        print(form)
        if form.is_valid(): 
            user = form.save()
            login(request, user)
            return redirect('/')
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})
