
import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="D.I.F", page_icon="🧠")
st.title("D.I.F")

def get_n8n_response(question, chat_history):
    webhook_url = os.getenv("WEBHOOK_URL")
    
    if not webhook_url:
        return "WEBHOOK_URL이 설정되지 않았습니다."

    data = {
        "question": question,
        "chat_history": chat_history
    }
    
    try:
        response = requests.post(webhook_url, json=data, verify=False)
        response.raise_for_status()
        # n8n 응답 구조에 따라 "assistant" 역할의 답변만 추출
        # 실제 n8n 응답을 확인하고 이 부분을 조정해야 할 수 있습니다.
        n8n_data = response.json()
        # 예시: 응답이 {'answer': '...'} 형태일 경우
        if isinstance(n8n_data, dict) and 'answer' in n8n_data:
            return n8n_data.get("answer", "응답이 없습니다.")
        # 예시: 응답이 단순 텍스트일 경우
        else:
            return str(n8n_data) # 혹은 response.text

    except requests.exceptions.RequestException as e:
        return f"n8n 워크플로우 호출에 실패했습니다: {e}"
    except ValueError: # JSON 디코딩 실패 시
        return f"n8n 응답을 처리할 수 없습니다: {response.text}"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("D.I.F에 질문하기"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # 이전 대화 기록을 n8n으로 전달
        chat_history = [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages]
        
        full_response = get_n8n_response(prompt, chat_history)
        message_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})
