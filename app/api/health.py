from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def home():
    return {"message": "home"}


@router.get("/health")
async def health():
    return {"message": "normal"}
