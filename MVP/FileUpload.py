import streamlit as st
import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

# 환경 변수에서 설정 읽기
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_BLOB_CONTAINER = os.getenv("AZURE_BLOB_CONTAINER")

st.title("Azure Blob Storage 파일 업로드")

uploaded_file = st.file_uploader("파일을 선택하세요", type=None)

if uploaded_file is not None:
    try:
        # BlobServiceClient 생성
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(AZURE_BLOB_CONTAINER)

        # 파일 업로드
        blob_client = container_client.get_blob_client(uploaded_file.name)
        blob_client.upload_blob(uploaded_file, overwrite=True)

        st.success(f"{uploaded_file.name} 파일이 업로드되었습니다.")
    except Exception as e:
        st.error(f"업로드 실패: {e}")