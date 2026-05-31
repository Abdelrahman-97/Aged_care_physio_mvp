from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_route import router as auth_router
from routes.resident_routes import router as resident_router
from routes.progress_notes_route import router as progress_notes_router
from routes.assessment_route import router as assessment_router
from routes.chart_routes import router as chart_router
from pandas_routes import user_pandas_router, resident_pandas_router, assessment_pandas_router

app = FastAPI(title="Aged Care Physio MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(resident_router)
app.include_router(progress_notes_router)
app.include_router(assessment_router)
app.include_router(chart_router)
app.include_router(user_pandas_router)
app.include_router(resident_pandas_router)
app.include_router(assessment_pandas_router)

@app.get("/")
def root():
    return "Backend is live"
