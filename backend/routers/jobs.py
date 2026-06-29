from fastapi import APIRouter

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

@router.get("/")
def jobs_home():
    return {
        "message": "Jobs API Working"
    }