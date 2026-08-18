import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "Active",
        "message": "Welcome to Sports Prediction & Safe Odds API"
    }

@app.get("/api/predictions/safe")
def get_safe_odds():
    # Safe Odds Strategy (2.00 - 5.00)
    return {
        "ticket_type": "Daily Safe Ticket",
        "target_odds": 3.15,
        "matches": [
            {"sport": "Football", "match": "Real Madrid vs Getafe", "prediction": "Home Win", "odds": 1.35},
            {"sport": "Football", "match": "Arsenal vs Wolves", "prediction": "Over 1.5 Goals", "odds": 1.25},
            {"sport": "Basketball", "match": "LA Lakers vs Golden State", "prediction": "Lakers +6.5", "odds": 1.86}
        ]
    }

@app.get("/api/predictions/mega")
def get_mega_accumulator():
    # Mega Accumulator Strategy (Up to 500.98)
    return {
        "ticket_type": "Mega Accumulator",
        "target_odds": 500.98,
        "total_matches": 12,
        "matches": [
            {"sport": "Football", "match": "Man City vs Everton", "prediction": "Home Win", "odds": 1.28},
            {"sport": "Basketball", "match": "Boston Celtics vs Miami Heat", "prediction": "Over 215.5 Points", "odds": 1.75},
            {"sport": "Football", "match": "Bayern Munich vs Leipzig", "prediction": "Both Teams to Score", "odds": 1.55}
            # Mfumo utaongeza mechi zingine kiotomatiki kupitia API
        ]
    }
  
