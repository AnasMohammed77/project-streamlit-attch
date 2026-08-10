import joblib 
import pandas as pd
import numpy as np
import time
from fastapi import FastAPI
from pydantic import BaseModel
model=joblib.load("Model.pkl")
encoder=joblib.load("Encoder.pkl")
ordinal_encoder=joblib.load("ordinal_encoder.pkl")
app = FastAPI()
class Data(BaseModel):
   service:str
   sbytes:float
   dbytes:float
   sttl:float
   dttl:float
   sload:float
   dload:float
   smean:float
   dmean:float
   ct_srv_src:float
   ct_state_ttl:float
   ct_dst_src_ltm:float
   ct_srv_dst:float
@app.post("/predict")
def prediction(data:Data):
   start_time=time.perf_counter()
#to array data
   data_pred=np.array([
   data.service,
   data.sbytes,
   data.dbytes,
   data.sttl,
   data.dttl,
   data.sload,
   data.dload,
   data.smean,
   data.dmean,
   data.ct_srv_src,
   data.ct_state_ttl,
   data.ct_dst_src_ltm,
   data.ct_srv_dst
   ])
   #prediction
   data_pred[0]=float(ordinal_encoder.transform([[data_pred[0][0:]]])[0][0])
   predict=model.predict([data_pred])
   attack_name = encoder.inverse_transform(predict)[0]
   probablity=model.predict_proba([data_pred]).max()*100
   probablity=round(probablity,2)
   end_time=time.perf_counter()
   total_time=end_time-start_time
   print( total_time)


   return {
      "attach":attack_name,
      "probability":probablity,
      "total_time":total_time
   }



# @app.post("/predict")
# def prediction(
#    service:str,
#    sbytes:float,
#    dbytes:float,
#    sttl:float,
#    dttl:float,
#    sload:float,
#    dload:float,
#    smean:float,
#    dmean:float,
#    ct_srv_src:float,
#    ct_state_ttl:float,
#    ct_dst_src_ltm:float,
#    ct_srv_dst:float
# ):

#    data=[
#       service,sbytes,dbytes,sttl,dttl,sload,dload,
#       smean,dmean,ct_srv_src,ct_state_ttl,ct_dst_src_ltm,ct_srv_dst

#    ]
#    print(data)

#    data[0]=float(ordinal_encoder.transform([[data[0]]])[0][0])
#    data=np.array(data)
#    print(data)
#    predict=model.predict([data])
#    attack_name = encoder.inverse_transform(predict)[0]
#    probablity=model.predict_proba([data]).max()*100
#    probablity=round(probablity,2)
#    return{
#    "attack_name":attack_name,
#     "probability":probablity
#     }
