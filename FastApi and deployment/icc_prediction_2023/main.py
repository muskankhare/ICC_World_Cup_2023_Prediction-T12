from fastapi import FastAPI, Query, Form
from pydantic import BaseModel, ValidationError, validator
from enum import Enum
import pandas as pd
import numpy as np
import pickle

match_predictor = './finalist_prediction.pkl'
app = FastAPI()

# Enum for team names
class TeamA(str, Enum):
    SouthAfrica = "South Africa"
    Australia = "Australia"
    India = "India"
    England = "England"
    NewZealand = "New Zealand"
    Pakistan = "Pakistan"
    Netherlands = "Netherlands"
    Afghanistan = "Afghanistan"
    Bangladesh = "Bangladesh"
    SriLanka = "Sri Lanka"

# Enum for team names
class TeamB(str, Enum):
    India = "India"
    Australia = "Australia"
    SouthAfrica = "South Africa"
    England = "England"
    NewZealand = "New Zealand"
    Pakistan = "Pakistan"
    Netherlands = "Netherlands"
    Afghanistan = "Afghanistan"
    Bangladesh = "Bangladesh"
    SriLanka = "Sri Lanka"

# Enum for venue names (Add more as needed)
class VenueT(str, Enum):
    NarendraModiStadium = "Narendra Modi Stadium, Ahmedabad"
    WankhedeStadium = "Wankhede Stadium, Mumbai"
    EdenGardens = "Eden Gardens, Kolkata"
    HyderabadStadium = "Rajiv Gandhi International Stadium, Uppal, Hyderabad"
    DharamsalaStadium = "Himachal Pradesh Cricket Association Stadium, Dharamsala"
    DelhiStadium = "Arun Jaitley Stadium, Delhi"
    ChennaiStadium = "MA Chidambaram Stadium, Chepauk, Chennai"
    LucknowStadium = "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow"
    PuneStadium = "Maharashtra Cricket Association Stadium, Pune"
    BengaluruStadium = "M Chinnaswamy Stadium, Bengaluru"

# Pydantic model for input data with validation
class InputData(BaseModel):
    venue: VenueT
    batting_team: TeamA
    bowling_team: TeamB
    ball: float
    cum_runs: int
    wickets_remaining: int
    run_rate: float
    required_run_rate: float
    ball_left: int
    runs_needed: int
    target: int

    @validator("ball")
    def validate_ball(cls, value):
        if not 0 <= value <= 50:
            raise ValueError("Ball must be a float between 0 and 50.")
        return round(value, 1)

    @validator("run_rate", "required_run_rate")
    def validate_run_rate(cls, value):
        if not 0 <= value <= 80:
            raise ValueError("Run rate must be a float between 0 and 80.")
        return round(value, 2)

    @validator("wickets_remaining")
    def validate_integer_range(cls, value):
        if not 0 <= value <= 10 and isinstance(value, int):
            raise ValueError("Integer values must be in the range 0 to 10.")
        return value
    
    @validator("ball_left")
    def validate_integer_range(cls, value):
        if not 0 <= value <= 300 and isinstance(value, int):
            raise ValueError("Integer values must be in the range 0 to 10.")
        return value
    
    @validator("target")
    def validate_integer_range(cls, value):
        if not 0 <= value <= 1 and isinstance(value, int):
            raise ValueError("Integer values must be in the range 0 to 10.")
        return value
    
    @validator("cum_runs", "required_run_rate", "runs_needed")
    def validate_integer_range(cls, value):
        if not 0 <= value <= 1000 and isinstance(value, int):
            raise ValueError("Integer values must be in the range 0 to 10.")
        return value

@app.get("/")
def read_root():
    return {"Team Name" : "Team 12-Gold Diggers",
            "Task ":"ICC World Cup 2023 predictions"}

@app.post("/predict")
def predict(
    venue: VenueT = Form(...),
    batting_team: TeamA = Form(...),
    bowling_team: TeamB = Form(...),
    ball: float = Form(0.1),
    cum_runs: int = Form(0),
    wickets_remaining: int = Form(10),
    run_rate: float = Form(6),
    required_run_rate: float = Form(0),
    ball_left: int = Form(299),
    runs_needed: int = Form(0),
    target: int = Form(0),
):
    
    data = InputData(
        venue=venue,
        batting_team=batting_team,
        bowling_team=bowling_team,
        ball=ball,
        cum_runs=cum_runs,
        wickets_remaining=wickets_remaining,
        run_rate=run_rate,
        required_run_rate=required_run_rate,
        ball_left=ball_left,
        runs_needed=runs_needed,
        target=target,
    )

    if bowling_team == batting_team :
        print("Teams are the same!")
        result = {"error": "Batting and bowling team cannot be same",
              "statement" : "Please Confirm Batting team and balling team ",
              }
        
        return result
    

    # Convert the input data to a DataFrame
    input_df = pd.DataFrame([data.dict()])

    with open(match_predictor, 'rb') as file:
        model = pickle.load(file)

    # Make predictions
    predictions = model.predict(input_df)

    predicted_probabilities = model.predict_proba(input_df)

    #probabilities for winning (class 1)
    probabilities_class_1 = predicted_probabilities[:, 1]

    ans = ''
    if predictions == 1 or predictions == '1':
        ans = batting_team + " will win" 
    
    else:
        ans = bowling_team + " will win" 

    # Assuming the model returns a single prediction for each row
    result = {"predictions": predictions.tolist(),
              "statement" : ans,
              "Predicted winning Probabilities for Batting team" : probabilities_class_1[:5].tolist()
              }

    return result
