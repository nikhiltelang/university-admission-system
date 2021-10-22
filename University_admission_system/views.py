import re
import io
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from University_admission_system.templatetags import CassandraOperation, EmailOperation, logger, pdfwriter
import uuid
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

cdb = CassandraOperation.CassandraManagement()
def home(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def signin(request):
    if request.method == 'POST':
        signintype = request.POST['signintypeselect']
        email = request.POST['SigninInputEmail1']
        passw = request.POST['SigninInputPassword1']
        cdb = CassandraOperation.CassandraManagement()
        if signintype=='faculty':
            result ,data= cdb.faculty_signin(email,passw)
            return render(request,'faculty_page.html',{"result":result,"data":data})
        else:
            result = cdb.student_signin(email,passw)
            data = result
            for i in data:
                id = str(i.id)
            return render(request,'student_info.html',{"result":result,"id":id})


def signup(request):
    if request.method=='POST':
        signuptype = request.POST['signuptypeselect']
        fname = request.POST.get('SignupInputFullName')
        email = request.POST.get('SignupInputEmail1')
        pass1 = request.POST.get('SignupInputPassword1')
        pass2 = request.POST.get('SignupInputPassword2')
        id = uuid.uuid4()
        cdb = CassandraOperation.CassandraManagement()
        
        if signuptype == "faculty":
            msg = cdb.faculty_registration(id,fname,email,pass1)
        else:
            msg = cdb.student_registration(id,fname,email,pass1)
        # if pass1 != pass2:
        #     messages.error(request,'Password must be same')
        # myuser = User.objects.create_user(username=username,email=email,password=pass1)
        # myuser.first_name = fname
        # myuser.last_name = lname
        # myuser.save()
        # messages.success(request,'Your account have been Created')
        print(signuptype,fname,email,pass1,pass2)
        return render(request,'login.html')

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

def faculty_profile_page(request,id):
    id = uuid.UUID(id)
    cdb = CassandraOperation.CassandraManagement()
    data = cdb.faculty_profile_data(id)
    return render(request,'faculty_profile.html',{"id":id,"data1":data[0],"data2":data[1],"data3":data[2]})

def view(request,id):
    
    cdb = CassandraOperation.CassandraManagement()
    personal_data = cdb.select_student_info(id)
    return render(request,'view.html',{"personal_data":personal_data[0],"religion_data":personal_data[1],"caste_data":personal_data[2],
        "income_data":personal_data[3],"domicile_data":personal_data[4],"paddress_data":personal_data[5],"caddress_data":personal_data[6],
        "past_education_data":personal_data[7],"applying_data":personal_data[8],"id":id})

def faculty_logout(request):
    return render(request,'index.html')

def student_logout(request):
    return render(request,'login.html')

def changepassword(request,id):
    if request.method=="POST":
        pass1 = request.POST.get("inputpassword1")
        pass2 = request.POST.get("inputpassword2")
        print(pass1,pass2)
        if pass1 != pass2:
            print("password not same")
        else:
            cdb.changepassword(pass1,id)
            return render(request,'student_info.html')

def insert_personal_data(request,id):
    if request.method=="POST":
        strid = request.POST.get('uuid')
        id = uuid.UUID(strid)
        Aadhar_card_no = request.POST.get('Aadhar_card_no')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        dateofbirth = request.POST.get('dateofbirth')
        age = request.POST.get('age')
        gender = request.POST.get("gender")
        Applicant_Full_Name_As_Per_SSC_Marksheet = request.POST.get('Applicant_Full_Name_As_Per_SSC_Marksheet')
        Guardian_Mobile_No = request.POST.get('Guardian_Mobile_No')
        Marital_Status = request.POST.get('Marital_Status')
        cdb = CassandraOperation.CassandraManagement()
        cdb.insert_personal_details(id,Aadhar_card_no,fullname,email,mobile,dateofbirth,age,gender,Applicant_Full_Name_As_Per_SSC_Marksheet,Guardian_Mobile_No,Marital_Status)
        return render(request,'religion_details.html',{"id":id})

def insert_religion_data(request,id):
    if request.method=="POST":
        strid = request.POST.get('uuid')
        id = uuid.UUID(strid)
        religion = request.POST.get('religion')
        cdb = CassandraOperation.CassandraManagement()
        cdb.insert_religion_details(id,religion)
        result = cdb.student_info(id)
        return render(request,'caste_details.html',{"id":id,"result":result[2]})

def insert_caste_data(request,id):
    if request.method=="POST":
        strid = request.POST.get('uuid')
        id = uuid.UUID(strid)
        Caste_Category = request.POST.get('Caste_Category')
        caste = request.POST.get('caste')
        Do_you_have_Caste_Certificate = request.POST.get('Do_you_have_Caste_Certificate')
        Caste_Certificate_Number = request.POST.get('Caste_Certificate_Number')
        Issuing_District = request.POST.get('Issuing_District')
        Applicant_Name = request.POST.get('Applicant_Name')
        Issuing_Authority = request.POST.get('Issuing_Authority')
        Caste_Certificate = request.POST.get('Caste_Certificate')
        Caste_Issuing_Date = request.POST.get('Caste_Issuing_Date')
        cdb = CassandraOperation.CassandraManagement()
        cdb.insert_caste_details(id,Caste_Category,caste,Do_you_have_Caste_Certificate,Caste_Certificate_Number,Issuing_District,Applicant_Name,Issuing_Authority,Caste_Certificate,Caste_Issuing_Date)
        result = cdb.student_info(id)
        return render(request,'income_details.html',{"id":id,"result":result[3]})

def insert_income_data(request,id):
    if request.method == "POST":
        strid = request.POST.get('uuid')
        id = uuid.UUID(strid)
        Family_Annual_Income = request.POST.get('Family_Annual_Income')
        Do_you_have_Income_Certificate = request.POST.get('Do_you_have_Income_Certificate')
        Income_Certificate_No = request.POST.get('Income_Certificate_No')
        Income_Issuing_Authority = request.POST.get('Income_Issuing_Authority')
        Income_Certificate = request.POST.get('Income_Certificate')
        Income_Issuing_Date = request.POST.get('Income_Issuing_Date')
        cdb = CassandraOperation.CassandraManagement()
        cdb.insert_income_details(id,Family_Annual_Income, Do_you_have_Income_Certificate, Income_Certificate_No, Income_Issuing_Authority, Income_Certificate, Income_Issuing_Date)
        result = cdb.student_info(id)
        return render(request,'domicile_details.html',{"id":id,"result":result[4]})
def insert_domicile_data(request,id):
    if request.method == "POST":
        strid = request.POST.get('uuid')
        id = uuid.UUID(strid)
        Are_you_Domicile_of_Maharashtra = request.POST.get('Are_you_Domicile_of_Maharashtra')
        Do_you_have_Domicile_Certificate = request.POST.get('Do_you_have_Domicile_Certificate')
        Relationship_Type = request.POST.get('Relationship_Type')
        Domicile_Certificate_No = request.POST.get('Domicile_Certificate_No')
        Applicant_Name = request.POST.get('Applicant_Name')
        Issuing_Authority = request.POST.get('Issuing_Authority')
        domicile_Issuing_Date = request.POST.get('domicile_Issuing_Date')
        Domicile_Certificate = request.POST.get('Domicile_Certificate')
        cdb = CassandraOperation.CassandraManagement()
        cdb.insert_domicile_details(id,Are_you_Domicile_of_Maharashtra, Do_you_have_Domicile_Certificate,Relationship_Type ,Domicile_Certificate_No, Applicant_Name, Issuing_Authority, domicile_Issuing_Date, Domicile_Certificate)
        result = cdb.student_info(id)
        return render(request,'address_details.html',{"id":id,"result":result[5],"result2":result[6]})

def insert_address_data(request,id):
    if request.method == "POST":
        strid = request.POST.get('uuid')
        id = uuid.UUID(strid)
        paddress = request.POST.get('paddress')
        pstate =request.POST.get('pstate')
        pdistrict = request.POST.get('pdistrict')
        ptaluka = request.POST.get('ptaluka')
        pvillage = request.POST.get('pvillage')
        ppincode = request.POST.get('ppincode')
        caddress = request.POST.get('caddress')
        cstate = request.POST.get('cstate')
        cdistrict = request.POST.get('cdistrict')
        ctaluka = request.POST.get('ctaluka')
        cvillage = request.POST.get('cvillage')
        cpincode = request.POST.get('cpincode')
        cdb = CassandraOperation.CassandraManagement()
        cdb.insert_address_details(id,paddress,pstate,pdistrict,ptaluka,pvillage,ppincode,caddress,cstate,cdistrict,ctaluka,cvillage,cpincode)
        result = cdb.student_info(id)
        return render(request,'past_education_details.html',{"id":id,"result":result[5]})


def insert_past_edu_data(request,id):
    if request.method == "POST":
        strid = request.POST.get('uuid')
        id = uuid.UUID(strid)
        qualification_level = request.POST.get('qualification_level')
        stream = request.POST.get('stream')
        completed = request.POST.get('completed')
        institute_state = request.POST.get('institute_state')
        institute_district = request.POST.get('institute_district')
        institute_taluka = request.POST.get('institute_taluka')
        college_school_name = request.POST.get('college_school_name')
        course = request.POST.get('course')
        board_university = request.POST.get('board_university')
        mode = request.POST.get('mode')
        Admission_Year = request.POST.get('Admission_Year')
        passing_year = request.POST.get('passing_year')
        result = request.POST.get('result')
        percentage = request.POST.get('percentage')
        Attempts = request.POST.get('Attempts')
        Upload_Marksheet = request.POST.get('Upload_Marksheet')

        cdb = CassandraOperation.CassandraManagement()
        cdb.insert_past_edu_details(id,qualification_level,stream,completed,institute_state,institute_district,institute_taluka,college_school_name,course,
                                             board_university,mode,Admission_Year,passing_year,result,percentage,Attempts,Upload_Marksheet)

        result = cdb.student_info(id)
        return render(request,'applying_details.html',{"id":id,"result":result[8]})

def insert_applying_data(request,id):
    if request.method == "POST":
        strid = request.POST.get('uuid')
        id = uuid.UUID(strid)
        apply_course_name = request.POST.get('apply_course_name')
        apply_Admission_Type = request.POST.get('apply_Admission_Type')
        apply_cet_percentage = request.POST.get('apply_cet_percentage')
        apply_cap_id = request.POST.get('apply_cap_id')
        apply_admission_through = request.POST.get('apply_admission_through')
        apply_gap_year = request.POST.get('apply_gap_year')
        apply_mode = request.POST.get('apply_mode')
        cdb = CassandraOperation.CassandraManagement()
        result = cdb.insert_applying_details(id,apply_course_name, apply_Admission_Type, apply_cet_percentage, apply_cap_id,apply_admission_through,apply_gap_year,apply_mode)

        pdf = pdfwriter.pdf()
        file = pdf.pdfwriter()

        buffer = io.BytesIO()
        # p = canvas.Canvas(buffer)
        # p.drawString(100, 500, "Hello Nikhil")
        # p.rect(inch, inch, 6 * inch, inch)
        # p.showPage()
        # p.save()
        # buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=file)

def personal_details(request,id):
    cdb = CassandraOperation.CassandraManagement()
    result = cdb.student_info(id)
    return render(request,'personal_details.html',{"id":id,"data":result[0]})

def religion_details(request,id):
    cdb = CassandraOperation.CassandraManagement()
    result = cdb.student_info(id)
    return render(request,'religion_details.html',{"id":id,"result":result[1]})

def caste_details(request,id):
    cdb = CassandraOperation.CassandraManagement()
    result = cdb.student_info(id)
    return render(request,'caste_details.html',{"id":id,"result":result[2]})

def income_details(request,id):
    cdb = CassandraOperation.CassandraManagement()
    result = cdb.student_info(id)
    return render(request,'income_details.html',{"id":id,"result":result[3]})

def domicile_details(request,id):
    cdb = CassandraOperation.CassandraManagement()
    result = cdb.student_info(id)
    return render(request,'domicile_details.html',{"id":id,"result":result[4]})

def address_details(request,id):
    cdb = CassandraOperation.CassandraManagement()
    result = cdb.student_info(id)
    return render(request,'address_details.html',{"id":id,"result":result[5]})

def past_education_details(request,id):
    cdb = CassandraOperation.CassandraManagement()
    result = cdb.student_info(id)
    return render(request,'past_education_details.html',{"id":id,"result":result[6]})

def applying_details(request,id):
    cdb = CassandraOperation.CassandraManagement()
    result = cdb.student_info(id)
    return render(request,'applying_details.html',{"id":id,"result":result[7]})

def approvedbyfaculty(request):
    mail = EmailOperation.EmailManagement()
    # result = mail.sendEmail('nikhiltelang70@gmail.com','nikhiltelang34@gmail.com','hello Niikhil')
    return render(request,'view.html')

def rejectbyfaculty(request):
    return HttpResponse("Rejeted by Faculty")

def selectbyfaculty(request):
    return HttpResponse("Selected By Faculty")

def caste_certificate_view(request):
    return HttpResponse("Caste Certificate View")

def income_view(request):
    return HttpResponse("Income View")

def domicile_view(request):
    return HttpResponse("Domicile View")

def ssc_certificate_view(request):
    return HttpResponse("SSC View")

def hsc_certificate_view(request):
    return HttpResponse("HSC View")

def get_info(request):
    return HttpResponse("Work is not done")

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def some_view(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(0, 0, "Hello world.")
    p.rect(inch, inch, 6 * inch, 9 * inch, fill=1)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='hello.pdf')