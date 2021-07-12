from django.db import models

# Created by Gaurab
class Employer(models.Model):
	emplo_id = models.AutoField(auto_created= True, primary_key=True, unique=True, help_text="Primary key for table")
	emplo_comname = models.CharField(max_length=100, unique=True, help_text="Company Name")
	emplo_number = models.CharField(max_length=10, unique=True, help_text="Employer Number")
	emplo_email = models.CharField(max_length=100, help_text="Email Address")
	emplo_occupation =  models.CharField(max_length = 200, help_text = 'Employer Occupation')

	def __str__(self):
		return str(self.emplo_comname)

# Created by Rhys
class jobAd(models.Model):

	jobId = models.AutoField( auto_created = True, primary_key=True, unique=True, help_text="Primary key for table")
	employer = models.ForeignKey(Employer, to_field='emplo_comname', null=True, on_delete=models.CASCADE, help_text="Foreign key to Employer table")
	jobTitle = models.CharField(max_length=100, help_text="Job Title")
	jobDescription = models.CharField(max_length=400, help_text="Job Description")
	dateAdded = models.DateTimeField(auto_now_add=True, help_text="Date added to site")
	salary = models.IntegerField(null = True, help_text="Offered salary for the job")

	def __str__(self):
		return str(self.jobTitle)



class Employee(models.Model):
	emp_id = models.AutoField( auto_created = True, primary_key=True, unique=True, help_text="Primary key for table")
	emp_fname = models.CharField(max_length=100, help_text="First Name")
	emp_lastname = models.CharField(max_length=100, help_text="Last Name")
	emp_qualification = models.CharField(max_length = 200, help_text = 'Qualification')
	emp_expectedsalary = models.CharField(max_length = 100, help_text = 'Expected Salary')
	emp_contact_no = models.CharField(max_length=10, help_text="Contact number")
	emp_email = models.CharField(max_length=100, help_text="Email Address")
	def __str__(self):
		return str(self.emp_id)


#created by Conner
class AppliedApplicants(models.Model):

	appliedId = models.AutoField( auto_created = True, primary_key=True, unique=True,)
	Employee_Id = models.ForeignKey(Employee,on_delete=models.CASCADE,)
	ad_ID = models.ForeignKey(jobAd,on_delete=models.CASCADE,)
	dateApplied = models.DateTimeField(auto_now_add=True,)
	moneyOffered = models.DecimalField(max_digits=7,decimal_places=0,default=0,)
	Add_duration = models.DecimalField(max_digits = 7,decimal_places=0,default=0, help_text="Duration in Weeks")

	def __str__(self):
		return self.adId






#gaurab7
