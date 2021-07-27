from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
def home(request):
    return render(request,'index.html')

# def contact(request):
#     print("jump here")
#     return

def signin(request):
    if request.method == 'POST':
        signintype = request.POST['signintypeselect']
        email = request.POST['SigninInputEmail1']
        passw = request.POST['SigninInputPassword1']
        # user = authenticate(username=usern, password=passw)
        print(signintype,email, passw)
        # if user is not None:
        #     login(request, user)
        #     print("success")
        #     messages.success(request, 'Successfully Logged In')
        #     return redirect('home')
        #
        # else:
        #     messages.error(request, 'Invalid Creditions')
        #     print("fail")
        #     return redirect('home')
        return HttpResponse("Login Successfully")


def signup(request):
    if request.method=='POST':
        signuptype = request.POST['signuptypeselect']
        fname = request.POST.get('SignupInputFullName')
        email = request.POST.get('SignupInputEmail1')
        pass1 = request.POST.get('SignupInputPassword1')
        pass2 = request.POST.get('SignupInputPassword2')
        # if pass1 != pass2:
        #     messages.error(request,'Password must be same')
        # myuser = User.objects.create_user(username=username,email=email,password=pass1)
        # myuser.first_name = fname
        # myuser.last_name = lname
        # myuser.save()
        # messages.success(request,'Your account have been Created')
        print(signuptype,fname,email,pass1,pass2)
        return HttpResponse("Signup Successfully")