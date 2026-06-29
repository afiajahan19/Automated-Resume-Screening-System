from fastapi import FastAPI

from database import Base, engine
import models

from routers import resume, jobs

# Create Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Automated Resume Screening System",
    version="1.0"
)

# Include Routers
app.include_router(resume.router)
app.include_router(jobs.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Automated Resume Screening System"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "database": "SQLite Connected"
    }