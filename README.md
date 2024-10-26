# Ex02 Django ORM Web Application
## Date: 27.10.24

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```

admin.py

from django.contrib import admin
from .models import Bank,BankAdmin
admin.site.register(Bank,BankAdmin)

models.py

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
```


## OUTPUT
![alt text](<Screenshot 2024-10-26 233348.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
