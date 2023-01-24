from django.db import models

# Create your models here.
class Department(models.Model):
    de_name=models.CharField(max_length=30)
    de_description=models.CharField(max_length=300)
    do_name=models.CharField(max_length=30)
    image = models.ImageField()

    def __str__(self):
        return self.de_name


class DoctorIn(models.Model):
    ID = models.AutoField(primary_key=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    image=models.ImageField()

    def __str__(self):
        return self.name



class Booking(models.Model):
    Token_id=models.AutoField(primary_key=True)
    date= models.DateTimeField(auto_now_add=True)
    Fullname=models.CharField(max_length=30)
    Email=models.EmailField()
    Phone=models.CharField(max_length=11)
    Age=models.CharField(max_length=2)
    Department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    Doctor=models.ForeignKey(DoctorIn,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.Fullname



