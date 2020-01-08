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

    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=40)
    Dependants = models.IntegerField()
    ApplicantIncome = models.IntegerField()
    CoapplicantIncome = models.IntegerField()
    Loan_Amount = models.IntegerField()
    Loan_Amount_Term = models.IntegerField()
    Credit_History = models.IntegerField()
    Gender = models.CharField(max_length=15, choices = GENDER_CHOICES)
    Married = models.CharField(max_length=15, choices = MARRIED_CHOICES)
    Education =  models.CharField(max_length=15, choices = GRADUATED_CHOICES)
    Self_Employed = models.CharField(max_length=15, choices = SELFEMPLOYED_CHOICES)
    Property_Area = models.CharField(max_length=15, choices = PROPERTY_CHOICES)
    


    def __str__(self):
        return '{}, {}'.format(self.Firstname, self.Lastname)
