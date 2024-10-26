from django.db import models
from django.contrib import admin
class Bank(models.Model):
	Name=models.CharField(max_length=20)
	Accountnum=models.IntegerField()
	Age=models.IntegerField()
	income=models.FloatField()
	Loanam=models.FloatField()
	Aadharnum=models.IntegerField(primary_key="Aadharnum")
	Email=models.EmailField()
class BankAdmin(admin.ModelAdmin):
	 list_display=('Name','Accountnum','Age','income','Loanam','Aadharnum','Email')