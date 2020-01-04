from django.db import models

# Create your models here.
class Approvals(models.Model):

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    MARRIED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    GRADUATED_CHOICES = (
        ('Graduated', 'Graduated'),
        ('Not Graduated', 'Not Graduated')
    )

    SELFEMPLOYED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('SemiUrban', 'SemiUrban'),
        ('Urban', 'Urban')
    )

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)
    dependants = models.IntegerField()
    applicantincome = models.IntegerField()
    coapplicantincome = models.IntegerField()
    loanamount = models.IntegerField()
    loanterm = models.IntegerField()
    credithistory = models.IntegerField()
    gender = models.CharField(max_length=15, choices = GENDER_CHOICES)
    married = models.CharField(max_length=15, choices = MARRIED_CHOICES)
    graduated =  models.CharField(max_length=15, choices = GRADUATED_CHOICES)
    selfemployed = models.CharField(max_length=15, choices = SELFEMPLOYED_CHOICES)
    area = models.CharField(max_length=15, choices = PROPERTY_CHOICES)

    def __str__(self):
        return self.firstname, self.lastname
