from django.db import models
from datetime import datetime

#photos=folder create inside media automatically
#%y=year create
#%m=month
#%d=date
#the labels are created below
#CharField used whenever numeric character both used 


#mvp=most valuable person

# Create your models here.
class Realtor(models.Model):
    name=models.CharField(max_length=200) 
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/') ##the photos will be kept inside photos folder
    description=models.TextField(max_length=200)#the entry should be done ,,if u will give 'blank=True' (then either u will give anything or not it will not show error) 
   ## phone_no=models.CharField(max_length=12)
    email=models.CharField(max_length=50)
    is_mvp=models.BooleanField(default=False)
    hire_date=models.DateTimeField(default=datetime.now,blank=True)
    

    def __str__(self):
        return self.name
