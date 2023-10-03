import uvicorn
import uvicorn
import pickle
from fastapi import FastAPI
from pydantic import BaseModel


class Machine(BaseModel):
    numerical__Load_cells: float
    numerical__Hydraulic_Pressure: float
    numerical__Coolant_Pressure: float
    numerical__Air_System_Pressure: float
    numerical__Coolant_Temperature: float
    numerical__Hydraulic_Oil_Temperature: float
    numerical__Proximity_sensors: float
    numerical__Spindle_Vibration: float
    numerical__Tool_Vibration: float
    numerical__Spindle_Speed: float
    numerical__Voltage: float
    numerical__Torque: float
    numerical__Cutting_Force: float
app = FastAPI()

with open("./naive_bayes.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def index():
    return {'message': 'This is the homepage of the API '}
  
@app.post("/prediction")
def get_machine_category(data: Machine):
    received = data.dict()
    numerical__Load_cells = received['numerical__Load_cells']
    numerical__Hydraulic_Pressure = received['numerical__Hydraulic_Pressure']
    numerical__Coolant_Pressure = received['numerical__Coolant_Pressure']
    numerical__Air_System_Pressure = received['numerical__Air_System_Pressure']
    numerical__Coolant_Temperature = received['numerical__Coolant_Temperature']
    numerical__Hydraulic_Oil_Temperature = received['numerical__Hydraulic_Oil_Temperature']
    numerical__Proximity_sensors = received['numerical__Proximity_sensors']
    numerical__Spindle_Vibration = received['numerical__Spindle_Vibration']
    numerical__Tool_Vibration = received['numerical__Tool_Vibration']
    numerical__Spindle_Speed = received['numerical__Spindle_Speed']
    numerical__Voltage = received['numerical__Voltage']
    numerical__Torque = received['numerical__Torque']
    numerical__Cutting_Force = received['numerical__Cutting_Force']
    pred_name = model.predict([[numerical__Load_cells, numerical__Hydraulic_Pressure, numerical__Coolant_Pressure,
                                numerical__Air_System_Pressure, numerical__Coolant_Temperature,
                                numerical__Hydraulic_Oil_Temperature,
                                numerical__Proximity_sensors, numerical__Spindle_Vibration,
                                numerical__Tool_Vibration, numerical__Spindle_Speed,
                                numerical__Voltage, numerical__Torque, numerical__Cutting_Force]]).tolist()[0]

    return {'prediction': pred_name}

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=4000)

    
