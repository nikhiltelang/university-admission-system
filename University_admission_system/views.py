from django.shortcuts import render
from django.http import HttpResponse
from University_admission_system.templatetags import CassandraOperation
# from templatetags import CassandraOperation

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
        if signintype=='faculty':
            return render(request,'faculty_page.html')
        else:
            cdb = CassandraOperation.CassandraManagement()
            print(cdb)
            return render(request,'student_info.html')


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

def faculty_change_password(request):
    if request.method=='POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        return HttpResponse("Password Change Successfully")

def faculty_home_page(request):
    return render(request,'faculty_page.html')

def faculty_profile_page(request):
    return render(request,'faculty_profile.html')

def view(request):
    return render(request,'view.html')