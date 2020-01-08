from django.shortcuts import render
from . forms import ApprovalForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import Approvals
from . serializers import ApprovalsSerializers
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd

#Grab anything in the model
#Serialize information
class ApprovalsView(viewsets.ModelViewSet):
	queryset = Approvals.objects.all()
	serializer_class = ApprovalsSerializers

def ohevalue(df):
    ohe_col1 = pd.read_csv("/Users/John Lang/Desktop/Learning/newtitles.csv")
    ohe_col = ohe_col1.columns
    cat_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    df_processed = pd.get_dummies(df, columns = cat_columns)
    new_dict = {}

    for i in ohe_col:
        if i in df_processed.columns:
            new_dict[i]=df_processed[i].values
        else:
            new_dict[i]=0
    newdf=pd.DataFrame(new_dict)
    return newdf

#Machine Learning Model
# @api_view(["POST"])
def approvereject(request):
    try:
        ohe_col1 = pd.read_csv("/Users/John Lang/Desktop/Learning/newtitles.csv")
        ohe_col = ohe_col1.columns
        mdl=joblib.load("/Users/John Lang/Desktop/Learning/loan_model.pkl")
        #mydata=pd.read_excel take dictionary and pull only the values, take as array and reshape
        mydata = request.data
        unit=np.array(list(mydata.values()))
        unit=unit.reshape(1,-1)
        scalers=joblib.load("/Users/John Lang/Desktop/Learning/scalers.pkl")
        X=scalers.transform(unit)
        y_pred=mdl.predict(X)
        y_pred=(y_pred>0.52)
        newdf=pd.DataFrame(y_pred, columns=['Status'])
    #Put to a data frame and predict, then identify as true or false on the target
        newdf=newdf.replace({True:'Approved', False:'Rejected'})
        return ('Your Status is {}'.format(newdf))
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def cxcontact(request):
    if request.method=='POST':
        form=ApprovalForm(data=request.POST)
        if form.is_valid():
            Firstname=form.cleaned_data['Firstname']
            Lastname=form.cleaned_data['Lastname']
            Dependants=form.cleaned_data['Dependants']
            ApplicantIncome=form.cleaned_data['ApplicantIncome']
            CoapplicantIncome=form.cleaned_data['CoapplicantIncome']
            Loan_Amount=form.cleaned_data['Loan_Amount']
            Loan_Amount_Term=form.cleaned_data['Loan_Amount_Term']
            Credit_History=form.cleaned_data['Credit_History']
            Gender=form.cleaned_data['Gender']
            Married=form.cleaned_data['Married']
            Education=form.cleaned_data['Education']
            Self_Employed=form.cleaned_data['Self_Employed']
            Property_Area=form.cleaned_data['Property_Area']

            form = form.save()
            form.save()

            myDict = (request.POST).dict()
            #Make Dictionary DF
            df=pd.DataFrame(myDict, index=[0])
            #Once in dict, call one-hot-encoding (ohe)

            print(approvereject(ohevalue(df)))
            print(ohevalue(df))
        else:
            print("error")

    form = ApprovalForm()

    return render(request, 'myform/cxform.html', {'form':form})
