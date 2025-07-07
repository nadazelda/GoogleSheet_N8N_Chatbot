# 🧠 D.I.F (Data Intelligence Finance)

## 📌 프로젝트 요약

GoogleSheet 기반 가계부 데이터를 Supabase Vector Store로 벡터화하여 OpenAI 기반 RAG로 자동 응답하는 개인 맞춤형 가계부 QA 시스템입니다.

- ETL 및 워크플로 관리: n8n
- LLM 기반 RAG 응답: OpenAI
- Vector Store: Supabase
- 사용자 UI: Streamlit
- HTTPS 연동: Cloudflare Tunnel
- 배포 환경: AWS EC2 + Docker + Docker Compose

---

## 📂 프로젝트 구조

/home/ec2-user/
├── n8n/
│   ├── docker-compose.yml         # n8n 컨테이너 배포
│   └── n8n_data/                  # n8n 워크플로 및 데이터 영구 저장 볼륨
└── streamlitChat/
    ├── app.py                     # Streamlit 사용자 UI
    ├── Dockerfile                 # Streamlit Docker 빌드용
    ├── docker-compose.yml         # Streamlit + Cloudflare Tunnel 배포
    ├── requirements.txt           # Streamlit 의존성
    └── .env                       # WEBHOOK_URL 등 환경 변수

---

## 🚀 주요 기능

- GoogleSheet 자동 연동 → Supabase 벡터화
- 사용자가 Streamlit UI에서 질문 시 OpenAI 기반 RAG 자동 응답
- 로딩 스피너 및 타이핑 애니메이션 출력
- Cloudflare Tunnel HTTPS 외부 접속
- n8n Function Node에서 Webhook JSON 파싱 후 AI Agent Node 전달
- 세션 기반 관리 및 대화 맥락 유지

---

## 🛠️ 사용 기술

Backend: n8n, OpenAI GPT-4o, Supabase, GoogleSheet  
Frontend: Streamlit  
Infra: AWS EC2, Docker, Docker Compose  
Network: Cloudflare Tunnel  
Vector DB: Supabase Embedding

---

## ⚡ 운영 방법

1. n8n 컨테이너 실행

cd ~/n8n  
docker compose up -d

2. Streamlit + Cloudflare 실행

cd ~/streamlitChat  
docker compose up -d --build

3. 상태 확인

docker ps -a  
docker logs -f n8n  
docker logs -f streamlit-app

4. 사용하지 않는 이미지/볼륨 정리

docker system prune -a -f --volumes

---

## 💡 연동 흐름

n8n: GoogleSheet → Supabase → Webhook Node → AI Agent Node → JSON 응답 반환

{
  "answer": "질문에 대한 답변"
}

Streamlit UI: 사용자 질문 입력 → n8n Webhook POST 요청

[
  {
    "sessionId": "<uuid>",
    "action": "sendMessage",
    "chatInput": "<질문>"
  }
]

응답 수신 후 로딩 및 타이핑 애니메이션 출력

Cloudflare Tunnel: Streamlit (localhost:8501) → HTTPS URL 외부 노출

---

## ✅ 유지보수 체크리스트

- n8n Webhook 및 워크플로 정상 작동
- Supabase 및 GoogleSheet 연동 확인
- Streamlit → n8n → 응답 → Streamlit 표시 확인
- Cloudflare Tunnel HTTPS 접근 확인
- EC2 메모리 및 디스크 상태 주기적 점검
- 컨테이너 OOM 및 자동 재시작 설정 확인

---

## 🌿 향후 개선 예정

- Cloudflare Tunnel 고정 인증 연동
- 사용자별 세션 및 개인화 관리
- LLM 캐싱 및 속도 최적화
- Slack/Telegram 알림 연동
- ETL 장애 자동 모니터링

---

## 📞 문의 및 피드백

유지 보수, 개선, 기능 확장 필요 시 언제든 문의해주세요.
