from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib import messages 

# Create your views here.



# for sign up
def signup(request):
    if request.method == 'POST':
        user = SignUpForm(request.POST)
        if user.is_valid():
            user.save()
        # fname = request.POST['first_name']
        # lname = request.POST['last_name']
        # username = request.POST['username']
        # email = request.POST['email']
        # user = authenticate(request, fname = fname ,lname = lname , username = username, email = email )
    else:
        user = SignUpForm()

    return render(request,'signup.html',{'form': user})

# for login

def loginpage(request): 
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request,'login.html',{'data':form})
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return HttpResponseRedirect('/logpage')
        else:
            return render(request, 'login.html', {'data': form}) 

# login page

def logpage(request):
    return render(request,'logpage.html')


# for change password

def changepass(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    print("🚀 ~ file: views.py ~ line 55 ~ request.user", request.user)
    # print("🚀 ~ file: views.py ~ line 55 ~ form", form)
    print("--------hdh----",request.POST)

    if form.is_valid():
        print("==============")
        form.save()

    return render(request,'changepass.html',{'form':form})