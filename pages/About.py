import streamlit as st
st.markdown(
        """
    <style>
div.stButton>button{
background-color:limegreen;
border:non ;
}

    </style>

    """,unsafe_allow_html=True)



col1,col2,col3,col4=st.columns(4)

with col1:
        if st.button("Home"):
            st.switch_page("Home.py")
with col2:
        if st.button("🛡️ Prediction"):
            st.switch_page("pages/Prediction.py")
with col3:
        if st.button("Model"):
            st.switch_page("pages/Model.py")

with col4:
        if st.button("About"):
            st.switch_page("pages/About.py")
st.markdown("""
<h2 style="border-radius:30px;text-align:center;background:cyan"> About the Project</h2>

""",unsafe_allow_html=True)

col_1,col_2,col_3=st.columns([1,5,1])
with col_2:
        st.image("imge.jpg")

st.markdown("""
    <div style="background:#9CA3AF;font-size:20px;padding:20px;border-radius:25px;">
    <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">

    <h3> Project Overview</h3>
    <i style="font-size:10px;">
    <p>          
            This project is an AI-based cybersecurity system designed to detect
            and classify cyber attacks by analyzing network traffic data using 
            Machine Learning techniques.
    </p>
    <p>            
            The system analyzes network traffic features and predicts whether the 
            traffic is normal or malicious. If an attack is detected, the system 
            identifies its type and provides the prediction confidence
    </p>  
    </i>
    </div>    
                
    <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">

    <h4> Project Objectives<h4>
    <i style="font-size:10px;">
    <ul style="padding:6px;font-size:20px"> <i>            
                    <li> Detect cyber attacks.</li>
                    <li>Classify attack types.</li>
                    <li>Display prediction confidence.</li>
                    <li>Provide a user-friendly interface.</li>
                    <li>Improve threat detection and response speed.</li>
                    </i>
                </ul>
    </i>
    </div>
    <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">
     <i style="font-size:10px;">
    <h1> Technologies Used</h1>
    <h2> 🐍 Python</h2>
    <p>
        Python is used as the main programming language for data processing, model 
        development, and application development
    </p>
    <h2> 🎨 Streamlit</h2>
    <p>
        Streamlit is used to build the interactive web interface for the system.
    </p>
            
    <h2> ⚡️ FastAPI</h2>
    <p>
        FastAPI is used to create the API that receives network data, processes it, 
        and communicates with the Machine Learning model.
    </p>

    <h2> 🤖 Scikit-learn</h2>
    <p>
        Scikit-learn is used for data preprocessing, model training, evaluation, and 
            prediction.
    </p>
    <h2> 🐼 Pandas</h2>
    <p>
        Pandas is used for loading, cleaning, processing, and analyzing the dataset.
    </p>
    </i>
    </div>
       <div style="text-align:center;border-radius:10px;border:2px dashed;">
        <h2 style="background:#00ffff;border-radius:25px;">Contact Me</h2>
                        <p style="border-radius:70px;background:#00ffff;text-decoration:none;"><a href="https://mailto:alsnwyansmhmdbdaljlyl@gmail.com"> @Emial.com</a></p>
                        <p style="border-radius:50px;background:#00ffff;text-decoration:none;"><i class="fa-brands fa-whatsapp"></i></i><a href="https://wa.me/967776713367">WhatsApp</a></a></p>
                        <p style="border-radius:50px;background:#00ffff;text-decoration:none;"><i class="fa-brands fa-facebook-messenger"></i> <a href="https://m.me/ans.mhmd.alsnwy">Messenger</a></p>
                        <p style="border-radius:50px;background:#00ffff;text-decoration:none"><i class="fa-brands fa-facebook-f"></i><a href="https://www.facebook.com/share/19Fw8BRK99/">Facebook</a></p>
                        <p style="border-radius:50px;background:#00ffff;text-decoration:none;"><i class="fab fa-telegram"></i> <a href="https://t.me/Anas_Alsanwy" target="_blank">Telegram</a></p>
        </div> 
        </i>
        </div>

    <div style="background:white;border:2px dashed;margin:50px 0;padding:10px;border-radius:30px;text-algin:center">
    <h4> Developed by:</h4>
                    
    <b>Student: Anas Mohammed Abd ALijalyl Saeed</b>
    <p>
            Department of Artificial Intelligence
            University of Taiz
    <p style="text-align:center;background-color:black;color:white">© 2026</p>
    </p>

    </div>   
    </div>
    """,unsafe_allow_html=True)
st.write("")
    if st.button("🔍 Prediction",width="stretch"):
                st.switch_page("pages/Prediction.py")

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
