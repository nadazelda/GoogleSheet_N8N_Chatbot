import streamlit as st
import requests
import os
import uuid
import time
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="가계부챗봇", page_icon="🧠")
st.title("가계부챗봇")

# 세션 ID 생성 및 유지
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

def get_n8n_response(user_input):
    webhook_url = os.getenv("WEBHOOK_URL")
    
    if not webhook_url:
        return "WEBHOOK_URL이 설정되지 않았습니다."

    # n8n AI Agent 요구 형식으로 전송
    data = [
        {
            "sessionId": st.session_state["session_id"],
            "action": "sendMessage",
            "chatInput": user_input
        }
    ]

    try:
        response = requests.post(webhook_url, json=data, verify=False)
        response.raise_for_status()
        
        n8n_data = response.json()
        

        # n8n 응답 구조에 따라 처리
        if isinstance(n8n_data, list) and len(n8n_data) > 0:
            item = n8n_data[0]
            # 예상: {"answer": "응답"} 형태라면
            if "answer" in item:
                return item["answer"]
            # 예상: {"content": "응답"} 형태라면
            elif "content" in item:
                return item["content"]
            elif "output" in item:
                return item["output"]
            else:
                return str(item)
        elif isinstance(n8n_data, dict) and "output" in n8n_data:
            return n8n_data["output"]
        else:
            return str(n8n_data)

    except requests.exceptions.RequestException as e:
        return f"n8n 워크플로우 호출에 실패했습니다: {e}"
    except ValueError:
        return f"n8n 응답을 처리할 수 없습니다: {response.text}"

# Streamlit Chat UI
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 렌더링
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력
if prompt := st.chat_input("가계부챗봇에 질문하기"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        with st.spinner("가계부챗봇 답변을 작성 중입니다..."):
            full_response = get_n8n_response(prompt)

        # 스트림(타이핑) 효과
        displayed_text = ""
        for char in full_response:
            displayed_text += char
            message_placeholder.markdown(displayed_text)
            time.sleep(0.02)  # 타이핑 속도 조절

    st.session_state.messages.append({"role": "assistant", "content": full_response})
