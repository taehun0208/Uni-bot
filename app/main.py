from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# refresh 토큰을 httpOnly 쿠키로 주고받으므로 allow_credentials=True 필수
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO(M1): auth / users / admin_users 라우터 구현 후 여기에 등록


@app.get("/health")
def health_check():
    return {"status": "ok"}
