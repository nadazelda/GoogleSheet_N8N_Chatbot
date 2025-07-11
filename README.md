# 🧠 가계부 LLM 챗봇구현

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

* /home/ec2-user/
* ├── n8n/
* │   ├── docker-compose.yml         # n8n 컨테이너 배포
* │   └── n8n_data/                  # n8n 워크플로 및 데이터 영구 저장 볼륨
* └── streamlitChat/
*    ├── app.py                     # Streamlit 사용자 UI
*    ├── Dockerfile                 # Streamlit Docker 빌드용
*    ├── docker-compose.yml         # Streamlit + Cloudflare Tunnel 배포
*    ├── requirements.txt           # Streamlit 의존성
*    └── .env                       # WEBHOOK_URL 등 환경 변수

---

## 🚀 주요 기능

- n8n MCP를 활용해서 GoogleSheet 엑셀 데이터를 → Supabase 벡터화
- n8n MCP를 활용해서 챗 모델을 구성
- 사용자가 Streamlit UI에서 질문 시 n8n의 웹훅 노드를 활용해 OpenAI 기반 RAG 자동 응답
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

## ⚡ 사전 환경설정
1. ec2서버 Docker 설치
2. n8n 컨테이너설치 
3. streamlit 사용자 화면 빌드 docker-compose를 통해 cloudflare까지 같이 설치 ( dokcer-compose.yml참고 )
4. n8n 실행 후 n8n 노드.json 파일 import 
   * 구글시트 인증, supbase인증, openai인증은 각자 셋팅해야합니다

   
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

<img width="1710" height="63" alt="image" src="https://github.com/user-attachments/assets/f374f8dc-4878-4673-8d0b-c094a5508eb5" />

이렇게 총 3가지 컨테이너가 실행돼야 정상 동작
* n8n : 벡터데이터 생성 + 사용자 챗봇 webhook 역할
* sreamlit : 사용자 화면 UI + n8n 노드와 통신
* cloudflare : 접속 url 제공 


4. 사용하지 않는 이미지/볼륨 정리

docker system prune -a -f --volumes

---


5. 실행확인
   cloudflare log 공개 url 접속
   <img width="1235" height="210" alt="image" src="https://github.com/user-attachments/assets/e42f2a62-f9f7-436a-b229-58161b1f3777" />

  streamlit 기반 초기페이지 
  <img width="1382" height="1059" alt="image" src="https://github.com/user-attachments/assets/017dedbb-e396-43f2-815a-ae46be1b57b8" />

  n8n 워크플로우 활성화 확인 
  <img width="1560" height="352" alt="image" src="https://github.com/user-attachments/assets/4931a430-b161-4602-958b-432cc2ddd395" />

  질의문 
  <img width="1253" height="702" alt="image" src="https://github.com/user-attachments/assets/dc0cc490-c100-4b13-b6df-b6b7e796b934" />

   
