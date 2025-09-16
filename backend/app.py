from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="The Cover Mock API",
    description="Professional public preview for odds, projections, and line moves.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/odds")
def get_odds():
    return {
        "game_id": "NFL20250101",
        "teams": ["NE", "NYJ"],
        "odds": {"NE": -120, "NYJ": +110}
    }

@app.get("/projections")
def get_projections():
    return {
        "game_id": "NFL20250101",
        "NE_win_prob": 0.58,
        "NYJ_win_prob": 0.42,
        "ev": {"NE": 4.2, "NYJ": -3.7}
    }

@app.get("/line-moves")
def get_line_moves():
    return {
        "game_id": "NFL20250101",
        "moves": [
            {"time": "2025-09-16T15:00:00Z", "NE": -120, "NYJ": +110},
            {"time": "2025-09-16T12:00:00Z", "NE": -115, "NYJ": +105}
        ]
    }