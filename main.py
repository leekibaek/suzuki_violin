import streamlit as st
import pandas as pd


v1_df = pd.read_csv("https://raw.githubusercontent.com/leekibaek/suzuki_violin/main/V1.csv", encoding = "utf-8")

st.title("Suzuki Violin Vol.1")

file_paths = v1_df["파일명"].to_list()
titles = v1_df["제목"].to_list()
tracks = v1_df["트랙번호"].to_list()
composers = v1_df["작곡자"].to_list()
tracks_nums = len(tracks)

# tabs = st.tabs(tracks)
tabs = st.tabs(titles)

for i in range(0, tracks_nums):
    with tabs[i]:
        col1, col2 = st.columns(2)
        with col2:
            st.header("곡듣기")
            st.write(f"{tracks[i]}: {titles[i]}")
            st.audio(f"./audio_files_/V1/{i+1}.mp3")
        with col1:
            st.header("작곡자 정보")
            st.write(f"작곡자 : {composers[i]}")
            st.write("(상세 내용은 업데이트 예정)")
        



