from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load Model
model = joblib.load('model.pkl')

# Not standardized or preprocessor was used

class ExerciseData(BaseModel):
    Gender: int
    Age: int
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float
    

@app.get('/')
def home():
    return {'message':'Burnt Calories Prediction API is running'}

@app.post('/predict')
def predict(data: ExerciseData):
    
    input_dict = data.model_dump()
    
    df = pd.DataFrame([input_dict])
    
    # Optional preprocessing
    # df = preprocessor.transform(df)
    
    prediction = model.predict(df)
    
    return{
        'Predicted calories burnt': float(prediction[0])
    }
    