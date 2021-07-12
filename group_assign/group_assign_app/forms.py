from django import forms
from django.forms import ModelForm
from .models import *

# Job Advertisement form
# Created by Rhys
class jobAdForm(forms.ModelForm):
	class Meta:
		model = jobAd
		fields = "__all__"
		exclude = ['jobId','dateAdded']

		#jobId = forms.IntegerField()
		#jobTitle = forms.CharField(max_length=100)
		#jobDescription = forms.CharField(max_length=400)
		#salary = forms.CharField(max_length=7)

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = "__all__"
		
# Applied Aplicants Section
class Applied_Aplicant_Form1(forms.ModelForm):
	class Meta:
		model= AppliedApplicants
		exclude=[]


class Applied_Aplicant_Form3(forms.Form):
		Aplication_ID = forms.IntegerField()
		
#Form created by gaurab
class EmployerForm(forms.ModelForm):
	class Meta:
		model = Employer
		fields = "__all__"
		
