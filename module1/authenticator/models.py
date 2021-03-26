from django.db import models

# Registration
class Reg(models.Model):
    username = models.CharField(max_length=50)
    password = models.TextField(max_length=20)
    mobile = models.IntegerField()
    dob = models.DateField('date of birth')

    #def __str__(self):
     #   return self.name
