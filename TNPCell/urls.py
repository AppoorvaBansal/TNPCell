

from django.contrib import admin
from django.urls import path,include
from Student import views as Student_Views
from Admin import views as Admin_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AdminDashboard/',include('Admin.urls')),
    path('Student/',include('Student.urls')),
    path('all_company_details/',Student_Views.show_Comapny,name='show_Company'),
]
