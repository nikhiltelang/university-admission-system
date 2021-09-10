from django.shortcuts import render
from django.http import HttpResponse
from University_admission_system.templatetags import CassandraOperation
import uuid
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
        cdb = CassandraOperation.CassandraManagement()
        if signintype=='faculty':
            result = cdb.faculty_signin(email,passw)
            print("result =",result)
            if result is None:
                print("no such result")
            return render(request,'faculty_page.html')
        else:
            result = cdb.student_signin(email,passw)
            return render(request,'student_info.html')


def signup(request):
    if request.method=='POST':
        signuptype = request.POST['signuptypeselect']
        fname = request.POST.get('SignupInputFullName')
        email = request.POST.get('SignupInputEmail1')
        pass1 = request.POST.get('SignupInputPassword1')
        pass2 = request.POST.get('SignupInputPassword2')
        id = uuid.uuid1()
        cdb = CassandraOperation.CassandraManagement()
        
        if signuptype == "faculty":
            msg = cdb.faculty_registration(id,fname,email,pass1)
            print(msg)
        else:
            msg = cdb.student_registration(id,fname,email,pass1)
            print(msg)
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
    cdb = CassandraOperation.CassandraManagement()
    data = cdb.select_admission_summery()
    data2 = data
    return render(request,'faculty_page.html',{"data":data,"data2":data2})

def faculty_profile_page(request):
    cdb = CassandraOperation.CassandraManagement()
    data = cdb.faculty_profile_data()
    return render(request,'faculty_profile.html',{"data1":data[0],"data2":data[1],"data3":data[2]})

def view(request):
    cdb = CassandraOperation.CassandraManagement()
    personal_data = cdb.select_student_info()
    return render(request,'view.html',{"personal_data":personal_data[0],"religion_data":personal_data[1],"caste_data":personal_data[2],
    "income_data":personal_data[3],"domicile_data":personal_data[4],"paddress_data":personal_data[5],"caddress_data":personal_data[6],
    "past_education_data":personal_data[7],"applying_data":personal_data[8]})

def faculty_logout(request):
    return render(request,'index.html')