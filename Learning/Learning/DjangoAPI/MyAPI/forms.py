from django.forms import ModelForm

from . models import Approvals

class ApprovalForm(ModelForm):
    class Meta:
        model=Approvals
        fields = '__all__'

# class MyForm(forms.Form):
#     firstname= forms.CharField(max_length=15)
#     lastname= forms.CharField(max_length=15)
#     dependants = forms.IntegerField()
#     applicantincome = forms.IntegerField()
#     coapplicantincome = forms.IntegerField()
#     loanamount = forms.IntegerField()
#     loanterm = forms.IntegerField()
#     credithistory = forms.IntegerField()
#     gender =  forms.ChoiceField(choices = [('Male', 'Male'),('Female', 'Female')])
#     married =  forms.ChoiceField(choices = [('Yes', 'Yes'),('No', 'No')])
#     graduated =   forms.ChoiceField(choices = [('Graduated', 'Graduated'),('Not Graduated', 'Not Graduated')])
#     selfemployed = forms.ChoiceField(choices = [('Yes', 'Yes'),('No', 'No')])
#     area =  forms.ChoiceField(choices = [('Rural', 'Rural'),('SemiUrban', 'SemiUrban'),('Urban', 'Urban')])
