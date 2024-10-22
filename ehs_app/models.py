from django.db import models

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    blood_type = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    medical_condition = models.CharField(max_length=255)
    doctor_assigned = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
