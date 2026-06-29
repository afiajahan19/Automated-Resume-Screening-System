from fastapi import APIRouter, UploadFile, File

from services.file_handler import save_resume

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
def upload_resume(file: UploadFile = File(...)):
    saved_path = save_resume(file)

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "location": saved_path
    }