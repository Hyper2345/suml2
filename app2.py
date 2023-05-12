# źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic)

import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

import pathlib
from pathlib import Path

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

def main():

	st.set_page_config(page_title="Health App")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://www.healthkart.com/connect/wp-content/uploads/2021/09/900x500_banner_HK-Connect_How-to-Improve-Heart-Health-_-Points-To-Keep-In-Mind.jpg")

	with overview:
		st.title("Health App")

	with left:
		wiek_slider = st.slider("Wiek", value=1, min_value=1, max_value=90)
		objawy_slider = st.slider("Objawy", min_value=1, max_value=5)
		choroby_wsp_slider = st.slider("Choroby wsp.", min_value=0, max_value=5)

	with right:
		wzrost_slider = st.slider("Wzrost", value=1, min_value=1, max_value=250)
		leki_slider = st.slider("Leki", min_value=1, max_value=4)

	data = [[wiek_slider, objawy_slider, choroby_wsp_slider, wzrost_slider, leki_slider]]
	health = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.subheader("Czy taka osoba dozna choroby serca?")
		st.subheader(("Tak" if health[0] == 0 else "Nie"))
		st.write("Pewność predykcji {0:.2f} %".format(s_confidence[0][health][0] * 100))

if __name__ == "__main__":
    main()
