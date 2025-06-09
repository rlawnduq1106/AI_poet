# pip install python-dotenv
# pip install langchain-openai
# pip install streamlit

import os
#from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI

# 환경변수 로드
#load_dotenv()

# Streamlit 앱 설정
st.title("인공지능 시인")

# API 키 확인
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY가 설정되지 않았습니다. .env 파일을 확인해주세요.")
    st.stop()

# ChatOpenAI 모델 초기화
try:
    chat_model = ChatOpenAI(
        openai_api_key=api_key,  
        model="gpt-3.5-turbo"  
    )
except Exception as e:
    st.error(f"AI 모델 초기화 중 오류가 발생했습니다: {e}")
    st.stop()

# 사용자 입력
subject = st.text_input("시의 주제를 입력해주세요")

# 주제가 입력되었을 때만 시 생성
if subject:
    st.write(f"시의 주제: {subject}")
    
    # 시 생성 버튼
    if st.button("시 생성하기") or subject:
        try:
            with st.spinner("시를 작성 중입니다..."):
                result = chat_model.invoke(f"{subject}에 대한 시를 써줘")
                st.write("### 생성된 시")
                st.write(result.content)
        except Exception as e:
            st.error(f"시 생성 중 오류가 발생했습니다: {e}")
else:
    st.info("시의 주제를 입력해주세요.")