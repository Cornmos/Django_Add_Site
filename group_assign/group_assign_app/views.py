from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
import datetime

def home(request):
    return render(request,'group_assign_app/home.html')

def load_emp_form(request):
    form = EmployeeForm
    return render(request, "group_assign_app/Employee/EmployeeForm.html", {'form': form})

def add_emp_form(request):
    form = EmployeeForm(request.POST)
    form.save()
    return HttpResponseRedirect(reverse('ShowEmployee'))


def show_emp_form(request):
    emp = Employee.objects.all
    return render(request, "group_assign_app/Employee/Show_emp.html", {'Employee': emp})

def edit_emp_form(request, id):
    emp = Employee.objects.get(emp_id=id)
    return render(request, "group_assign_app/Employee/Edit_emp.html", {'Employee': emp})


def update_emp_form(request, id):
    emp = Employee.objects.get(emp_id=id)
    form = EmployeeForm(request.POST, instance = emp)
    form.save()
    return HttpResponseRedirect(reverse('ShowEmployee'))

def delete_emp_form(request, id):
    emp = Employee.objects.get(emp_id=id)
    emp.delete()
    return render(request,'group_assign_app/home.html')

#Job advertisement functions created by Rhys
# Show all job listings view
def jobAdRead(request):
    jobs = jobAd.objects.all()
    print("My output",jobs)
    return render(request,'group_assign_app/jobs/job_read.html',{'jobs' : jobs})

# Create a new job view
def jobAdCreateView(request):
    form = jobAdForm()
    if request.method == 'POST':
        form = jobAdForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            form = jobAdForm()
    else:
        form = jobAdForm()
    return render(request,'group_assign_app/jobs/job_create.html', {'jobAdForm' : form})

# Updates an existing job
def jobAdUpdateView(request, jobId):
    job = jobAd.objects.get(pk = jobId)
    if request.method == 'POST':
        form = jobAdForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listJobs'))

    else:
        form = jobAdForm(instance = job)
    form = jobAdForm(initial={'title': 'jobTitle', 'Desc':'jobDescription', 'sal':'salary'}, instance=job)
    return render(request, 'group_assign_app/jobs/job_update.html', {'jobAdForm':form})

# Deletes an existing job
def jobAdDelete(request, jobId):
    if request.method == 'POST':
        job = jobAd.objects.get(pk = jobId)
        job.delete()
        return HttpResponseRedirect(reverse('listJobs'))

# Applied Aplicants Section
#Add delete search and update functions
def load_AppliedAplicants(request):
#form type is for html form to load
    formtype=1
    form_data = {'AppliedForm': Applied_Aplicant_Form1(), 'formtype': formtype }

    return render(request, 'group_assign_app/AppliedAplicants.html', form_data)


def load_AppliedAplicants4(request):

    formtype=4
    form_data = {'AppliedForm': Applied_Aplicant_Form3() , 'formtype': formtype }

    return render(request, 'group_assign_app/AppliedAplicants.html', form_data)



def new_Applied_Aplicant(request):
    if request.method != 'POST':
        return HttpResponseRedirect('/AppliedAplicants/')
    else:
        page_data={}
        form = Applied_Aplicant_Form1(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/SearchApplied/')
        else:
            page_data = {'val_errors': form.errors,}
    return render(request, 'group_assign_app/home.html', page_data)





def Update_Aplied_Aplicant(request):
    if request.method != 'POST':
        return HttpResponseRedirect('/AppliedAplicants2/')
    else:
        page_data={}
        form = Applied_Aplicant_Form3(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
        else:
            page_data = {'val_errors': form.errors,}
    return render(request, 'group_assign_app/home.html', page_data)

def Search_Applied_Aplicant(request):
    Apps = AppliedApplicants.objects.all()
    formtype=3
    return render(request,'group_assign_app/AppliedAplicants.html',{'Apps' : Apps, 'formtype': formtype })




def Del_Aplied_Aplicant(request):
    if request.method != 'POST':
        return HttpResponseRedirect('/AppliedAplicants2/')
    else:
        page_data={}
        form = Applied_Aplicant_Form3(request.POST)
        if form.is_valid():
            data= form.cleaned_data.get("Aplication_ID")
            delthis=AppliedApplicants.objects.filter(appliedId=int(data))
            delthis.delete()
            return HttpResponseRedirect('/home/')
        else:
            page_data = {'val_errors': form.errors,}
    return render(request, 'group_assign_app/base.html', page_data)

#created by gaurab

def load_emplo_form(request):
    form = EmployerForm
    return render(request, "group_assign_app/Employer/employerform.html", {'form': form})

def add_emplo_form(request):
    form = EmployerForm(request.POST)
    form.save()
    return HttpResponseRedirect(reverse('ShowEmployer'))


def show_emplo_form(request):
    emplo = Employer.objects.all
    return render(request, "group_assign_app/Employer/Show_emplo.html", {'Employer': emplo})


def edit_emplo_form(request, id):
    emplo = Employer.objects.get(emplo_id=id)
    return render(request, "group_assign_app/Employer/Edit_emplo.html", {'Employer': emplo})


def update_emplo_form(request, id):
    emplo = Employer.objects.get(emplo_id=id)
    form = EmployerForm(request.POST, instance = emplo)
    form.save()
    return HttpResponseRedirect(reverse('ShowEmployer'))

def delete_emplo_form(request, id):
    emp = Employer.objects.get(emplo_id=id)
    emp.delete()
    return render(request,'group_assign_app/home.html')

