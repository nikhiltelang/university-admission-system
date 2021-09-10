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
]