# back-end

FastAPI 기반 백엔드 프로젝트입니다. 팀원들이 빠르게 개발 환경을 맞출 수 있도록 간단한 구조와 실행 방법을 정리합니다.

## 프로젝트 구조

- app/main.py: FastAPI 앱 진입점
- app/api/: API 라우터 모음
- app/api/v1/: v1 API 분리
- app/api/v1/endpoints/: 엔드포인트 구현
- app/core/: 공통 설정
- app/schemas/: 요청/응답 스키마

## 개발 환경

- Python 3.10 이상 권장
- 가상환경 사용 권장

## 설치 및 실행

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp env.example .env
uvicorn app.main:app --reload
```

## 환경 변수

프로젝트 루트에 .env 파일을 만들고 아래 값을 사용합니다.

```env
HOST=0.0.0.0
PORT=8000
ENVIRONMENT=development
SECRET_KEY=change-me
```

## 기본 엔드포인트

- GET / : 서버 실행 확인
- GET /api/v1/health : 헬스 체크

## 참고

- VS Code 터미널에서 .env를 자동으로 읽으려면 설정에서 `python.terminal.useEnvFile`를 켜주세요.
