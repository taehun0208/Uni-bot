# UniBot Backend

UniBot(사내 챗봇 서비스) 백엔드입니다. 현재는 **초기 세팅(스캐폴딩 + 설정 + 인프라)** 까지 완료된 상태이며, 기능(M1 인증/계정 등)은 아직 구현 전입니다.

## 기술 스택

| 구분 | 선택 |
|---|---|
| 언어/프레임워크 | Python 3.12, FastAPI |
| ORM/마이그레이션 | SQLAlchemy 2.0 (async) + asyncpg, Alembic |
| DB / 캐시 | PostgreSQL 16, Redis 7 (redis-py async) |
| 인증 | PyJWT (HS256), bcrypt, msal (Microsoft Entra ID) |
| 설정 | pydantic-settings (.env) |
| 테스트 | pytest, pytest-asyncio, httpx |
| 인프라 | Docker Compose (postgres + redis) |

## 프로젝트 구조

```
app/
├── main.py                # FastAPI 앱, CORS (라우터는 구현 후 등록)
├── core/
│   ├── config.py          # pydantic-settings (.env 로드)
│   ├── security.py        # (예정) JWT 발급/검증, bcrypt, 비밀번호 정책
│   └── deps.py            # (예정) get_current_user, get_current_admin
├── db/
│   ├── session.py         # (예정) async engine/session
│   └── redis.py           # (예정) redis client
├── models/                # (예정) user.py, team.py
├── schemas/               # (예정) auth.py, user.py
├── api/                   # (예정) auth.py, users.py, admin_users.py
└── services/              # (예정) auth_service.py, user_service.py, ms_oauth.py
alembic/                   # 마이그레이션 스캐폴드 (async 템플릿, 마이그레이션 파일은 아직 없음)
tests/                     # pytest
scripts/seed_admin.py      # (예정) admin 계정 시드
docker-compose.yml         # postgres 16 + redis 7
.env.example               # 환경 변수 템플릿
requirements.txt
```

`(예정)` 표시 파일은 자리만 잡아둔 placeholder이며 내부는 TODO 주석만 있습니다.

## 개발 환경 세팅

### 1. Python 3.12 가상환경

Python 3.12 기준입니다. [uv](https://docs.astral.sh/uv/)가 있으면 3.12가 없어도 자동으로 받아줍니다.

```bash
# uv 사용 (권장)
uv venv venv --python 3.12
uv pip install --python venv/bin/python -r requirements.txt

# 또는 python3.12가 이미 설치되어 있다면
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. 환경 변수

```bash
cp .env.example .env
```

| 변수 | 설명 |
|---|---|
| DATABASE_URL | asyncpg URL (기본 `postgresql+asyncpg://unibot:unibot@localhost:5432/unibot`) |
| POSTGRES_HOST_PORT | docker compose가 노출할 postgres 호스트 포트 (기본 5432) |
| REDIS_URL | 기본 `redis://localhost:6379/0` |
| JWT_SECRET_KEY | `openssl rand -hex 32` 로 생성해 교체 |
| ACCESS_TOKEN_EXPIRE_MINUTES / REFRESH_TOKEN_EXPIRE_DAYS | 토큰 만료 (기본 60분 / 14일) |
| MS_CLIENT_ID / MS_CLIENT_SECRET / MS_TENANT_ID / MS_REDIRECT_URI | Microsoft Entra ID 앱 등록 값 |
| FRONTEND_URL | CORS 허용 origin (기본 `http://localhost:3000`) |
| COOKIE_SECURE | 개발 `false`, 운영 `true` |
| ADMIN_EMAIL / ADMIN_PASSWORD / ADMIN_NAME | admin 시드용 |

> 로컬에서 5432 포트를 이미 다른 postgres가 쓰고 있다면 `.env`에서 `POSTGRES_HOST_PORT`와 `DATABASE_URL`의 포트를 함께 바꿔주세요 (예: 5433).

### 3. 인프라 (postgres + redis)

```bash
docker compose up -d      # postgres는 healthcheck 포함
docker compose ps         # unibot-postgres (healthy), unibot-redis 확인
```

### 4. 서버 실행

```bash
venv/bin/uvicorn app.main:app --reload
# 또는 source venv/bin/activate 후 uvicorn app.main:app --reload
```

확인:

```bash
curl http://localhost:8000/health
# {"status":"ok"}
```

## DB 마이그레이션 (Alembic)

async 템플릿으로 스캐폴드만 생성된 상태입니다 (`alembic/versions/` 비어 있음). 모델 구현 후:

```bash
venv/bin/alembic revision --autogenerate -m "..."   # env.py에 Base.metadata 연결 필요 (TODO 주석 참고)
venv/bin/alembic upgrade head
```

## 현재 엔드포인트

- `GET /health` : 헬스 체크 (`{"status":"ok"}`)

인증/유저/어드민 API는 M1 구현 시 추가됩니다.

## 참고

- CORS는 `FRONTEND_URL` 단일 origin + `allow_credentials=True`로 설정되어 있습니다 (refresh 토큰 httpOnly 쿠키 전달용).
- `.env`는 git에 올리지 않습니다 (`.gitignore` 등록됨). 새 변수를 추가하면 `.env.example`도 함께 갱신해주세요.
