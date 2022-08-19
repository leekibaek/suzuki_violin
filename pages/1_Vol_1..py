import streamlit as st
import pandas as pd

vol = "Vol 01"

st.set_page_config(
    page_title = f"Suzuki Violin - {vol}"
)


df = pd.read_csv("https://raw.githubusercontent.com/leekibaek/suzuki_violin/main/Vs.csv", encoding = "utf-8")
sub_df = df[df["권수"] == vol]

st.title(f"{vol}  🎻")


"---"

titles = sub_df["제목"].to_list()
composers = sub_df["작곡자"].to_list() 


for i,title in enumerate(titles):
    with st.expander(f"{i + 1}  -  {title}"):
        "---"
        col1, col2 = st.columns(2)
        with col1:
            st.header("Play")
            st.write(f"{titles[i]}")
            st.write("Play 속도를 조절할 수 있습니다😀")
            st.audio(f"./audio_files_/V1/{i+1}.mp3")
        with col2:
            st.header("Info.")
            st.write(f"작곡자 : {composers[i]}")
            st.write("(상세 내용은 업데이트 예정)")