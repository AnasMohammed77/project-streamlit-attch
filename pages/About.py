import streamlit as st



col1,col2,col3,col4=st.columns(4)

with col1:
        if st.button("Home"):
            st.switch_page("index.py")
with col2:
        if st.button("🛡️ Prediction"):
            st.switch_page("pages/predict.py")
with col3:
        if st.button("Model"):
            st.switch_page("pages/model.py")

with col4:
        if st.button("About"):
            st.switch_page("pages/About.py")


col_1,col_2,col_3=st.columns([1,3,1])
with col_2:
        st.image("imge.jpg",width=500)

st.markdown("""
## About the Project

### AI-Based Cyber Attack Detection and Classification System
""")

st.markdown("""
### Project Overview
            
        This project is an AI-based cybersecurity system designed to detect
         and classify cyber attacks by analyzing network traffic data using 
         Machine Learning techniques.
        The system analyzes network traffic features and predicts whether the 
         traffic is normal or malicious. If an attack is detected, the system 
         identifies its type and provides the prediction confidence
### Project Objectives
1- Detect cyber attacks.

2- Classify different attack types.

3- Analyze network traffic.

4- Provide prediction confidence.

5- Provide a simple and user-friendly interface.
## Technologies Used
### 🐍 Python

    Python is used as the main programming language for data processing, model 
     development, and application development
### 🎨 Streamlit
    Streamlit is used to build the interactive web interface for the system.
            
### ⚡️ FastAPI
    FastAPI is used to create the API that receives network data, processes it, 
     and communicates with the Machine Learning model.
            

### 🤖 Scikit-learn

    Scikit-learn is used for data preprocessing, model training, evaluation, and 
        prediction.
### 🐼 Pandas

    Pandas is used for loading, cleaning, processing, and analyzing the dataset.

""")
st.markdown("""
    <div style="border:2px dashed;margin:50px 0;padding:10px;border-radius:30px;text-algin:center">
    <h4> Developed by:</h4>
                
    <b>Student: Anas Mohammed Abd ALijalyl Saeed</b>
    <p>
        Department of Artificial Intelligence
        University of Taiz
                <p style="text-align:center;background-color:black;color:white">© 2026</p>
    </p>

    </div>
    """,unsafe_allow_html=True)