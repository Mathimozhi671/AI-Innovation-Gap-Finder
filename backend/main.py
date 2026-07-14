from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import Routes
from routes.search import router as search_router
from routes.github import router as github_router

app = FastAPI(
    title="AI Innovation Gap Finder API",
    version="1.0.0"
)

# -------------------------------
# Register Routers
# -------------------------------
app.include_router(search_router)
app.include_router(github_router)

# -------------------------------
# Enable CORS
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Request Model
# -------------------------------
class IdeaRequest(BaseModel):
    idea: str

# -------------------------------
# Home Route
# -------------------------------
@app.get("/")
def home():
    return {
        "message": "Welcome to AI Innovation Gap Finder API"
    }

# -------------------------------
# Health Check
# -------------------------------
@app.get("/health")
def health():
    return {
        "status": "Backend Running Successfully"
    }

# -------------------------------
# Analyze Route (Temporary)
# -------------------------------
@app.post("/analyze")
def analyze(data: IdeaRequest):
    return {
        "idea": data.idea,
        "existingSolutions": [
            "YOLO-based detection",
            "CNN disease classifiers",
            "Mobile diagnosis apps"
        ],
        "limitations": [
            "Requires large datasets",
            "Poor performance in low light",
            "Limited explainability"
        ],
        "innovationGaps": [
            "Predict disease before symptoms",
            "Offline AI diagnosis",
            "Explainable crop recommendations"
        ]
    }