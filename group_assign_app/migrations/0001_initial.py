# Generated by Django 3.2 on 2021-05-24 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(auto_created=True, help_text='Primary key for table', primary_key=True, serialize=False, unique=True)),
                ('emp_fname', models.CharField(help_text='First Name', max_length=100)),
                ('emp_lastname', models.CharField(help_text='Last Name', max_length=100)),
                ('emp_qualification', models.CharField(help_text='Qualification', max_length=200)),
                ('emp_expectedsalary', models.CharField(help_text='Expected Salary', max_length=100)),
                ('emp_contact_no', models.CharField(help_text='Contact number', max_length=10)),
                ('emp_email', models.CharField(help_text='Email Address', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('emplo_id', models.AutoField(auto_created=True, help_text='Primary key for table', primary_key=True, serialize=False, unique=True)),
                ('emplo_comname', models.CharField(help_text='Company Name', max_length=100, unique=True)),
                ('emplo_number', models.CharField(help_text='Employer Number', max_length=10, unique=True)),
                ('emplo_email', models.CharField(help_text='Email Address', max_length=100)),
                ('emplo_occupation', models.CharField(help_text='Employer Occupation', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='jobAd',
            fields=[
                ('jobId', models.AutoField(auto_created=True, help_text='Primary key for table', primary_key=True, serialize=False, unique=True)),
                ('jobTitle', models.CharField(help_text='Job Title', max_length=100)),
                ('jobDescription', models.CharField(help_text='Job Description', max_length=400)),
                ('dateAdded', models.DateTimeField(auto_now_add=True, help_text='Date added to site')),
                ('salary', models.IntegerField(help_text='Offered salary for the job', null=True)),
                ('employer', models.ForeignKey(help_text='Foreign key to Employer table', null=True, on_delete=django.db.models.deletion.CASCADE, to='group_assign_app.employer', to_field='emplo_comname')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedApplicants',
            fields=[
                ('appliedId', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('dateApplied', models.DateTimeField(auto_now_add=True)),
                ('moneyOffered', models.DecimalField(decimal_places=0, default=0, max_digits=7)),
                ('Add_duration', models.DecimalField(decimal_places=0, default=0, help_text='Duration in Weeks', max_digits=7)),
                ('Employee_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group_assign_app.employee')),
                ('ad_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group_assign_app.jobad')),
            ],
        ),
    ]
