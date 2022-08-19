import streamlit as st
import pandas as pd


st.set_page_config(
    page_title = "Hello"
)


st.write("# Welcome to My site! 🎻")             


st.markdown(
    """
    ---

    ### 이곳은 Suzuki Violin의 음원을 들을 수 있는 Site 입니다.

   
    **👈 사이드바에 있는 교재의 Volume 번호**를 선택하시면 음원 목록을 확인 할 수 있습니다.

    #### [**Volume List**]

    - Volume 1
    - Volume 2
    - Volume 3
    - Volume 4
    - Volume 5
    - Volume 6 (준비중)
    - Volume 7
    - Volume 8 (일부 누락)

    음원 재생시 속도 조절이 가능합니다.

    각 곡마다 작곡가 정보를 입력할 예정입니다.
    
"""
)
