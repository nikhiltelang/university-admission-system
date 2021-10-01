from django.conf.urls import url, include
from University_admission_system import views
from django.urls import path, re_path
urlpatterns = [
    url(r'^$', views.home,name='home'),
    # path('contact',views.contact,name='contact')
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('faculty_change_passsword',views.faculty_change_password,name='faculty_change_passsword'),
    path('faculty_home_page',views.faculty_home_page,name='faculty_home_page'), 
    path('faculty_profile_page',views.faculty_profile_page,name='faculty_profile_page'),
    path('view',views.view,name='view'),
    path('faculty_logout',views.faculty_logout,name='faculty_logout'),
    path('insert_personal_details',views.insert_personal_data,name="insert_personal_details"),
    path('insert_religion_details',views.insert_religion_data,name="insert_religion_details"),
    path('insert_caste_details',views.insert_caste_data,name="insert_caste_details"),
    path('insert_income_details',views.insert_income_data,name="insert_income_details"),
    path('insert_domicile_details',views.insert_domicile_data,name="insert_domicile_details"),
    path('insert_address_details',views.insert_address_data,name="insert_address_details"),
    path('insert_past_education_details',views.insert_past_edu_data,name="insert_past_education_details"),
    path('insert_applying_details',views.insert_applying_data,name="insert_applying_details"),
]