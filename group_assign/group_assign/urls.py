"""group_assign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from group_assign_app import views

urlpatterns = [
	re_path(r'^$',views.home),
	re_path(r'^home/?$',views.home,name='home'),
	re_path(r'^jobs/?$',views.jobAdCreateView,name='jobs'),
   	re_path(r'^jobs/createjob/?$',views.jobAdCreateView,name='jobs'),
   	re_path(r'^jobs/listjobs/?$',views.jobAdRead,name='listJobs'),
	path('jobs/update/<int:jobId>/', views.jobAdUpdateView, name='jobAdUpdate'),
	path('jobs/delete/<int:jobId>/', views.jobAdDelete, name='jobAdDelete'),
	re_path(r'^employee/load_emp_form/?$', views.load_emp_form, name = 'loadEmployee'),
	re_path(r'^employee/add_emp_form/?$', views.add_emp_form, name = 'AddEmployee'),
	re_path(r'^employee/show_emp_form/?$', views.show_emp_form, name = 'ShowEmployee'),
	path('employee/edit_emp_form/<int:id>', views.edit_emp_form, name = 'EditEmployee'),
	path('update_emp_form/<int:id>', views.update_emp_form, name = 'UpdateEmployee'),
	path('employee/delete_emp_form/<int:id>', views.delete_emp_form, name = 'DeleteEmployee'),
	path('admin/', admin.site.urls),
	re_path(r'^AppliedAplicants/?$',views.load_AppliedAplicants,name='AppliedAplicants'),
	re_path(r'^AppliedAplicants4/?$',views.load_AppliedAplicants4,name='AppliedAplicants4'),
    re_path(r'^AddApplied/?$',views.new_Applied_Aplicant,name='newapplied'),
	re_path(r'^UpdateApplied/?$',views.Update_Aplied_Aplicant,name='Updateapplied'),
	re_path(r'^SearchApplied/?$',views.Search_Applied_Aplicant,name='Searchapplied'),
	re_path(r'^DelApplied/?$',views.Del_Aplied_Aplicant,name='Delapplied'),
	re_path(r'^employer/load_emplo_form/?$', views.load_emplo_form, name = 'loadEmployer'),
	re_path(r'^employer/add_emplo_form/?$', views.add_emplo_form, name = 'AddEmployer'),
	re_path(r'^employer/show_emplo_form/?$', views.show_emplo_form, name = 'ShowEmployer'),
	path('employer/edit_emplo_form/<int:id>', views.edit_emplo_form, name = 'EditEmployer'),
	path('update_emplo_form/<int:id>', views.update_emplo_form, name = 'UpdateEmployer'),
	path('employer/delete_emplo_form/<int:id>', views.delete_emplo_form, name = 'DeleteEmployer'),
	
]
