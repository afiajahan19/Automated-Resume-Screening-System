from fastapi import APIRouter

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

@router.get("/")
def resume_home():
    return {
        "message": "Resume API Working"
    }