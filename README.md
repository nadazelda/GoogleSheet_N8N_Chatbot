📌 프로젝트 요약
✅ 프로젝트명: 🧠 D.I.F (Data Intelligence Finance)

✅ 목적:
GoogleSheet 기반 가계부 데이터를 Supabase Vector Store로 벡터화
OpenAI 기반 RAG를 사용해 사용자가 Streamlit UI에서 질의하면 자동으로 응답
n8n을 통한 ETL 및 워크플로 관리, Supabase, OpenAI, GoogleSheet 완전 연동
Cloudflare Tunnel을 통해 HTTPS로 외부 접속 가능

✅ 배포 및 운영 환경:
AWS EC2 (Ubuntu)
Docker + Docker Compose 기반 완전 자동화 배포
Streamlit 사용자 UI + n8n 컨테이너 분리 운영
Cloudflare Tunnel로 HTTPS 무료 연동



/home/ec2-user/
├── n8n/
│   ├── docker-compose.yml         # n8n 컨테이너 배포
│   └── n8n_data/                  # n8n 워크플로 및 데이터 영구 저장 볼륨
│
└── streamlitChat/
    ├── app.py                     # Streamlit 사용자 UI
    ├── Dockerfile                 # Streamlit Docker 빌드용
    ├── docker-compose.yml         # Streamlit + Cloudflare Tunnel 배포
    ├── requirements.txt           # Streamlit 의존성
    └── .env                       # WEBHOOK_URL 등 환경 변수


🛠️ 사용 기술
Backend: n8n, OpenAI GPT-4o, Supabase, GoogleSheet
Frontend: Streamlit (타이핑 애니메이션, 로딩 스피너 포함)
Infra: AWS EC2, Docker, Docker Compose
Network: Cloudflare Tunnel HTTPS 연동
Vector Store: Supabase Embedding


🚀 주요 기능
✅ GoogleSheet 자동 연동 → Supabase로 데이터 벡터화
✅ 사용자 질의 시 OpenAI 기반 RAG 자동 응답
✅ Streamlit 사용자 UI에서 실시간 대화
✅ 응답 시 로딩 스피너 + 스트리밍(타이핑) 효과
✅ Cloudflare Tunnel HTTPS 접근으로 외부 접속 가능
✅ n8n Function Node에서 Webhook JSON 파싱 → AI Agent Node 전달 및 응답 관리
✅ 세션 기반 관리 및 대화 맥락 유지 가능




⚡ 운영 방법
1️⃣ n8n 컨테이너 배포
cd ~/n8n
docker compose up -d
2️⃣ Streamlit + Cloudflare 배포
  cd ~/streamlitChat
  docker compose up -d --build
3️⃣ 상태 확인
  docker ps -a
  docker logs -f n8n
  docker logs -f streamlit-app
4️⃣ 불필요한 이미지/컨테이너 정리
  docker system prune -a -f --volumes
💡 주요 연동 흐름
1️⃣ n8n:
  GoogleSheet → Supabase Embedding → Webhook Node → AI Agent Node
  응답을 JSON 형태로 반환:

2️⃣ Streamlit 사용자 UI:
  사용자 입력 → n8n Webhook POST 호출:

3️⃣ Cloudflare Tunnel:
  Streamlit 컨테이너 http://localhost:8501 을 HTTPS URL로 외부 노출.

