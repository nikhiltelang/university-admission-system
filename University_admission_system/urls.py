from django.conf.urls import url, include
from University_admission_system import views
from django.urls import path, re_path
urlpatterns = [
    url(r'^$', views.home,name='home'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('faculty_change_passsword',views.faculty_change_password,name='faculty_change_passsword'),
    path('faculty_home_page',views.faculty_home_page,name='faculty_home_page'), 
    path('faculty_profile_page/<str:id>',views.faculty_profile_page,name='faculty_profile_page'),
    path('view/<str:id>',views.view,name='view'),
    path('faculty_logout',views.faculty_logout,name='faculty_logout'),
    path('student_logout',views.student_logout,name='student_logout'),
    path('changepassword/<str:id>',views.changepassword,name='changepassword'),
    path('insert_personal_details/<str:id>',views.insert_personal_data,name="insert_personal_details"),
    path('insert_religion_details/<str:id>',views.insert_religion_data,name="insert_religion_details"),
    path('insert_caste_details/<str:id>',views.insert_caste_data,name="insert_caste_details"),
    path('insert_income_details/<str:id>',views.insert_income_data,name="insert_income_details"),
    path('insert_domicile_details/<str:id>',views.insert_domicile_data,name="insert_domicile_details"),
    path('insert_address_details/<str:id>',views.insert_address_data,name="insert_address_details"),
    path('insert_past_education_details/<str:id>',views.insert_past_edu_data,name="insert_past_education_details"),
    path('insert_applying_details/<str:id>',views.insert_applying_data,name="insert_applying_details"),
    path('personal_details/<str:id>',views.personal_details,name="personal_details"),
    path('religion_details/<str:id>',views.religion_details,name="religion_details"),
    path('caste_details/<str:id>',views.caste_details,name="caste_details"),
    path('income_details/<str:id>',views.income_details,name="income_details"),
    path('domicile_details/<str:id>',views.domicile_details,name="domicile_details"),
    path('address_details/<str:id>',views.address_details,name="address_details"),
    path('past_education_details/<str:id>',views.past_education_details,name="past_education_details"),
    path('applying_details/<str:id>',views.applying_details,name="applying_details"),
    path('approvedbyfaculty',views.approvedbyfaculty,name="approvedbyfaculty"),
    path('rejectbyfaculty',views.rejectbyfaculty,name="rejectbyfaculty"),
    path('selectbyfaculty',views.selectbyfaculty,name="selectbyfaculty"),
    path('caste_certificate_view',views.caste_certificate_view,name="caste_certificate_view"),
    path('income_view',views.income_view,name="income_view"),
    path('domicile_view',views.domicile_view,name="domicile_view"),
    path('ssc_certificate_view',views.ssc_certificate_view,name="ssc_certificate_view"),
    path('hsc_certificate_view',views.hsc_certificate_view,name="hsc_certificate_view"),
    path('get_info',views.get_info,name="get_info"),

]