from django.shortcuts import render
from . forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import approvals
from . serializers import approvalsSerializers
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


#Machine Learning Model
@api_view(["POST"])
def approvereject(request):
	try:
		mdl=joblib.load("/Users/John Lang/Desktop/Learning/DjangoAPI/loan_model.pkl")
		#mydata=pd.read_excel take dictionary and pull only the values, take as array and reshape
		mydata=request.data
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		scalers=joblib.load("/Users/John Lang/Desktop/Learning/DjangoAPI/scalers.pkl")
		X=scalers.transform(unit)
		y_pred=mdl .predict(X)
		y_pred=(y_pred>0.52)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
        #Put to a data frame and predict, then identify as true or false on the target
		newdf=newdf.replace({True:'Approved', False:'Rejected'})
		return JsonResponse('Your Status is {}'.format(newdf), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
