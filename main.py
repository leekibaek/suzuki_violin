import streamlit as st
import pandas as pd


v1_df = pd.read_csv("https://raw.githubusercontent.com/leekibaek/suzuki_violin/main/V1.csv", encoding = "utf-8")

st.title("Suzuki Violin Vol.1")

file_paths = v1_df["파일명"].to_list()
titles = v1_df["제목"].to_list()
tracks = v1_df["트랙번호"].to_list()
composers = v1_df["작곡자"].to_list()
tracks_nums = len(tracks)

tabs = st.tabs(tracks)

for i in range(0, tracks_nums):
    with tabs[i]:
        col1, col2 = st.columns(2)
        with col2:
            st.header("곡듣기")
            st.write(f"{tracks[i]}: {titles[i]}")
            st.audio("./audio_files/V1/" + file_paths[i])
        with col1:
            st.header("작곡자 정보")
            st.write(f"작곡자 : {composers[i]}")
            st.write("(상세 내용은 업데이트 예정)")
        

# with tabs[0]:
#     "sdfsdf"

# with tabs[1]:
#     "tsdd"
# for i, title, file_path in enumerate(titles, file_paths):
#     with tabs[i]:
#         st.write(f"곡제목 : {title}")
#         st.audio(file_path)

# st.tabs(tracks)
# st.tabs(tracks_nums)
# for i, track in enumerate(tracks):
    
