import time
import streamlit as st
import keras
from PIL import Image
from getModel import teachable_machine_classification

st.title = "닮은 동물상 찾기"
st.header("본인의 사진을 올려 닮은 동물을 찾아보세요")
st.text("사진을 올려보세요")

uploaded_file = st.file_uploader("사진을 넣어주세요 ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='사진을 넣는중', use_column_width=True)
    st.write()
    with st.spinner( "분석중..."):
        time.sleep(5)
    label = teachable_machine_classification(image, 'keras_model.h5')
    if label == 0:
        st.success("거북이 상입니다")
    elif label == 1 :
        st.success("고래 상입니다")
    elif label == 2 :
        st.success("고양이 상입니다")
    elif label == 3 :
        st.success("개 상입니다")
    elif label == 4 :
        st.success("여우 상입니다")
    elif label == 5 :
        st.success("토끼 상입니다")
