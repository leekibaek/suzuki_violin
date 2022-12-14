import streamlit as st
import pandas as pd

vol = "Vol 01"

st.set_page_config(
    page_title = f"Suzuki Violin - {vol}"
)


df = pd.read_csv("https://raw.githubusercontent.com/leekibaek/suzuki_violin/main/Vs.csv", encoding = "utf-8")
sub_df = df[df["κΆμ"] == vol]

st.title(f"{vol}  π»")


"---"

titles = sub_df["μ λͺ©"].to_list()
composers = sub_df["μκ³‘μ"].to_list() 


for i,title in enumerate(titles):
    with st.expander(f"{i + 1}  -  {title}"):
        "---"
        col1, col2 = st.columns(2)
        with col1:
            st.header("Play")
            st.write(f"{titles[i]}")
            st.write("Play μλλ₯Ό μ‘°μ ν  μ μμ΅λλ€π")
            st.audio(f"./audio_files_/V1/{i+1}.mp3")
        with col2:
            st.header("Info.")
            st.write(f"μκ³‘μ : {composers[i]}")
            st.write("(μμΈ λ΄μ©μ μλ°μ΄νΈ μμ )")