import streamlit as st


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="About - Cyber Attack Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================
# CSS
# =========================

st.markdown("""
<style>

    /* Main container */
    .block-container {
        max-width: 1400px;
        padding: 2rem 5%;
        margin: auto;
    }

    /* Navigation buttons */
    div.stButton > button {
        width: 100%;
        min-height: 45px;
        background-color: limegreen;
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background-color: #32CD32;
        color: white;
        border: none;
    }

    /* Main title */
    .page-title {
        text-align: center;
        background-color: cyan;
        padding: 12px;
        border-radius: 30px;
        margin: 20px 0;
    }

    /* Cards */
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 25px;
        margin: 15px 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        font-size: 17px;
        line-height: 1.7;
    }

    .card h2,
    .card h3,
    .card h4 {
        margin-top: 5px;
    }

    /* Contact section */
    .contact {
        text-align: center;
        border: 2px dashed #555;
        padding: 20px;
        border-radius: 25px;
        margin-top: 30px;
    }

    .contact h2 {
        background-color: cyan;
        padding: 10px;
        border-radius: 25px;
    }

    .contact a {
        display: block;
        background-color: cyan;
        color: black;
        text-decoration: none;
        padding: 10px;
        margin: 10px auto;
        border-radius: 50px;
        max-width: 400px;
    }

    .contact a:hover {
        background-color: #00bfbf;
    }

    /* Developer section */
    .developer {
        background-color: white;
        border: 2px dashed #555;
        margin: 50px 0;
        padding: 20px;
        border-radius: 30px;
        text-align: center;
    }

    .copyright {
        background-color: black;
        color: white;
        padding: 8px;
        border-radius: 10px;
        margin-top: 15px;
    }


    /* =========================
       Tablet
       ========================= */

    @media (max-width: 900px) {

        .block-container {
            padding-left: 3%;
            padding-right: 3%;
        }

        .card {
            padding: 20px;
            font-size: 16px;
        }

    }


    /* =========================
       Mobile
       ========================= */

    @media (max-width: 600px) {

        .block-container {
            padding-left: 15px;
            padding-right: 15px;
            padding-top: 1rem;
        }

        .page-title {
            font-size: 24px;
            padding: 10px;
        }

        .card {
            padding: 15px;
            border-radius: 18px;
            font-size: 15px;
        }

        .card h2 {
            font-size: 22px;
        }

        .card h3 {
            font-size: 20px;
        }

        .card h4 {
            font-size: 18px;
        }

        div.stButton > button {
            min-height: 42px;
            font-size: 14px;
        }

        .contact {
            padding: 15px;
        }

        .developer {
            padding: 15px;
        }

    }

</style>
""", unsafe_allow_html=True)


# =========================
# Navigation
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Home"):
        st.switch_page("Home.py")

with col2:
    if st.button("🛡️ Prediction"):
        st.switch_page("pages/Prediction.py")

with col3:
    if st.button("📊 Model"):
        st.switch_page("pages/Model.py")

with col4:
    if st.button("ℹ️ About"):
        st.switch_page("pages/About.py")


# =========================
# Page Title
# =========================

st.markdown("""
<h2 class="page-title">
    About the Project
</h2>
""", unsafe_allow_html=True)


# =========================
# Project Image
# =========================

col_1, col_2, col_3 = st.columns([1, 5, 1])

with col_2:
    st.image(
        "imge.jpg",
        use_container_width=True
    )


# =========================
# Project Overview
# =========================

st.markdown("""
<div class="card">
<h3>Project Overview</h3>
<p>
        This project is an AI-based cybersecurity system designed to detect
        and classify cyber attacks by analyzing network traffic data using
        Machine Learning techniques.
</p>
<p>
        The system analyzes network traffic features and predicts whether the
        traffic is normal or malicious. If an attack is detected, the system
        identifies its type and provides the prediction confidence.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# Project Objectives
# =========================

st.markdown("""
<div class="card">

<h3>Project Objectives</h3>

<ul>
        <li>Detect cyber attacks.</li>
        <li>Classify attack types.</li>
        <li>Display prediction confidence.</li>
        <li>Provide a user-friendly interface.</li>
        <li>Improve threat detection and response speed.</li>
</ul>

</div>
""", unsafe_allow_html=True)


# =========================
# Technologies Used
# =========================

st.markdown("""
<div class="card">

<h3>Technologies Used</h3>

<h4>🐍 Python</h4>

<p>
        Python is used as the main programming language for data processing,
        model development, and application development.
</p>


<h4>🎨 Streamlit</h4>

<p>
        Streamlit is used to build the interactive web interface for the system.
</p>


<h4>⚡ FastAPI</h4>

<p>
        FastAPI is used to create the API that receives network data,
        processes it, and communicates with the Machine Learning model.
</p>


<h4>🤖 Scikit-learn</h4>

<p>
        Scikit-learn is used for data preprocessing, model training,
        evaluation, and prediction.
</p>


<h4>🐼 Pandas</h4>

<p>
        Pandas is used for loading, cleaning, processing, and analyzing
        the dataset.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# Contact Me
# =========================



# =========================
# Prediction Button
# =========================

st.write("")

if st.button("🔍 Prediction", width="stretch"):
    st.switch_page("pages/Prediction.py")


st.markdown("""
<div class="contact">

<h2>Contact Me</h2>

<a href="mailto:alsnwyansmhmdbdaljlyl@gmail.com">
        📧 Email
</a>

<a href="https://wa.me/967776713367">
        📱 WhatsApp
</a>

<a href="https://m.me/ans.mhmd.alsnwy">
        💬 Messenger</a>

<a href="https://www.facebook.com/share/19Fw8BRK99/">
        👍 Facebook
    </a>

<a href="https://t.me/Anas_Alsanwy" target="_blank">
        ✈️ Telegram
</a>

</div>
""", unsafe_allow_html=True)
# =========================
# Developer
# =========================

st.markdown("""
<div class="developer">

<h4>Developed by:</h4>

<b>
        Student: Anas Mohammed Abd ALijalyl Saeed
</b>

<p>
        Department of Artificial Intelligence<br>
        University of Taiz
</p>
<div class="copyright">
        © 2026
</div>

</div>
""", unsafe_allow_html=True)
