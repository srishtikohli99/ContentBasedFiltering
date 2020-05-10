#from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from uploadapp import serializers
from .serializers import HelloSerializer
import requests
import time
import os
from .reco import *
import numpy as np
import os
import joblib
from sklearn.preprocessing import MinMaxScaler
dir_path = os.path.dirname(os.path.realpath(__file__))
dirs = os.path.join(dir_path,"X1.npy")
X = np.load(dirs,allow_pickle=True)
import pyrebase
import sklearn
import sklearn.metrics

config = {
    "apiKey": "AIzaSyD_jhgmfiRT2lo4gnpWMZy8UBgUGErsX8U",
    "authDomain": "customer-2e919.firebaseapp.com",
    "databaseURL": "https://customer-2e919.firebaseio.com",
    "projectId": "customer-2e919",
    "storageBucket": "customer-2e919.appspot.com",
    "messagingSenderId": "345832555767",
    "appId": "1:345832555767:web:88ec6218e7c3c263c2fff2",
    "measurementId": "G-0X3YPL8H78"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
scaler1=joblib.load(os.path.join(dir_path,"fam_size"))
scaler2=joblib.load(os.path.join(dir_path,"age"))
# x = db.child("101").child("new").get().val()
# if x==1:
#     print("YES")

def recom(x):
    
    j=0
    age= db.child(x).child("age").get().val()
    print(age)
    fam_size= db.child(x).child("fam_size").get().val()
    print(fam_size)
    loc= db.child(x).child("loc").get().val()
    print(loc)
    gender = db.child(x).child("gender").get().val()
    print(gender)
    f=np.array([[fam_size]])
    a=np.array([[age]])
    fam_size=scaler1.transform(f)[0][0]
    age=scaler2.transform(a)[0][0]
    print(fam_size)
    print(age)
    if gender=="Female":
        gender=1
    else:
        gender=0
    Y=np.zeros(15)
    Y[0]=age 
    Y[1]=gender
    Y[2]=fam_size
    if loc=='Delhi':
        j=11
    elif loc=='New York':
        j=12
    elif loc=='Mumbai':
        j=13
    elif loc =='LA':
        j=14

    Y[j]=1
    # print(Y)
    Y=[Y]
    Y=np.array(Y)
    print(Y)
    euc = sklearn.metrics.pairwise.euclidean_distances(X, Y) 
    index=np.argmin(euc)
    print(X[index])
    return index



class FileUploadView(APIView):
    #parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
        
        url_serializer = HelloSerializer(data=request.data)
        serializer_class = serializers.HelloSerializer
        serializer =HelloSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.validated_data.get('obj')
            x = db.child(obj).child("new").get().val()
            if x==1:
                index=recom(obj)
                print(index+1)
            
            # print(rec_items)
            return Response("hi", status=status.HTTP_201_CREATED)


