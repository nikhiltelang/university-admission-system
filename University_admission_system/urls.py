from django.conf.urls import url, include
from University_admission_system import views
from django.urls import path
urlpatterns = [
    url(r'^$', views.home,name='home'),
    # path('contact',views.contact,name='contact')

]