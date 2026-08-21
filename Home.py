import streamlit as st


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="AI Cyber Attack Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

    /* =========================
       Main Container
       ========================= */

    .block-container {
        max-width: 1400px;
        background-color: #F5F5F5;
        padding: 2rem 5%;
        margin: auto;
    }


    /* =========================
       Navigation Buttons
       ========================= */

    div.stButton > button {
        width: 100%;
        min-height: 45px;
        background-color: limegreen;
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #32CD32;
        color: white;
        border: none;
    }


    /* =========================
       Main Title
       ========================= */

    .main-title {
        text-align: center;
        background-color: cyan;
        color: black;
        padding: 15px;
        border-radius: 30px;
        margin: 25px 0;
    }


    /* =========================
       Main Content
       ========================= */

    .main-content {
        background-color: #9CA3AF;
        padding: 20px;
        border-radius: 25px;
    }


    /* =========================
       Cards
       ========================= */

    .card {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        margin: 15px 0;
        font-size: 17px;
        line-height: 1.7;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .card h3 {
        color: blue;
        margin-top: 0;
    }


    /* =========================
       Statistics
       ========================= */

    .stats-title {
        color: blue;
        margin-bottom: 15px;
    }

    .stats-table {
        width: 100%;
        border-collapse: collapse;
        text-align: center;
        background-color: white;
        border-radius: 10px;
        overflow: hidden;
    }

    .stats-table th {
        background-color: rgb(255, 100, 120);
        padding: 12px;
    }

    .stats-table td {
        padding: 12px;
        border-bottom: 1px solid #ddd;
    }


    /* =========================
       Prediction Button
       ========================= */

    .prediction-container {
        margin-top: 25px;
        text-align: center;
    }


    /* =========================
       Developer
       ========================= */

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
       Mobile
       ========================= */

    @media (max-width: 600px) {

        .block-container {
            padding-left: 15px;
            padding-right: 15px;
            padding-top: 1rem;
        }

        .main-title {
            font-size: 23px;
            padding: 12px;
        }

        .main-content {
            padding: 12px;
            border-radius: 18px;
        }

        .card {
            padding: 15px;
            font-size: 15px;
        }

        .card h3 {
            font-size: 19px;
        }

        .stats-table {
            font-size: 13px;
        }

        .stats-table th,
        .stats-table td {
            padding: 8px 4px;
        }

        div.stButton > button {
            font-size: 14px;
            min-height: 42px;
        }

    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# Navigation
# =========================================================

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


# =========================================================
# Main Title
# =========================================================

st.markdown("""
<h4 class="main-title">
    🛡️ AI-Based Cyber Attack Detection and Classification System
</h4>
""", unsafe_allow_html=True)


# =========================================================
# Project Image
# =========================================================

col1, col2, col3 = st.columns([1, 3, 1])

with col2:

    st.image(
        "imge.jpg",
        use_container_width=True
    )


# =========================================================
# Main Content
# =========================================================

st.markdown("""
<div class="main-content">



<div class="card">

<h3>1. System Overview</h3>

<p>
                An intelligent system that leverages Machine Learning
                techniques to detect and classify cyber attacks by analyzing
                network traffic data.
</p>

<p>
                The system is designed to help cybersecurity professionals
                identify threats quickly and accurately.
</p>

</div>


<div class="card">

<h3>2. Project Objectives</h3>

<ul>
                <li>Detect cyber attacks.</li>
                <li>Classify attack types.</li>
                <li>Display prediction confidence.</li>
                <li>Provide a user-friendly interface.</li>
                <li>Improve threat detection and response speed.</li>
</ul>
</div>


<div class="card">

<h3>3. Model Information</h3>

<ul>
                <li><b>Algorithm:</b> Random Forest</li>
                <li><b>Dataset:</b> UNSW-NB15</li>
                <li><b>Number of Features:</b> 13 Features</li>
                <li><b>Number of Classes:</b> 10 Classes</li>
                <li><b>Task:</b> Multi-Class Classification</li>
</ul>

</div>


        

<div class="card">

<h3 class="stats-title"> 4. Quick Statistics</h3>

<table class="stats-table">

<tr>
                    <th>Metric</th>
                    <th>Value</th>
</tr>

<tr>
                    <td>📂 Total Samples</td>
                    <td>257,673</td>
</tr>
<tr>
                    <td>🛡️ Attack Categories</td>
                    <td>10</td>
</tr>

<tr>
                    <td>🎯 Model Accuracy</td>
                    <td>75.40%</td>
</tr>

<tr>
                    <td>⚡ Prediction Time</td>
                    <td>0.03 sec</td>
</tr>

</table>
</div>
</div>
    """, unsafe_allow_html=True)


# =========================================================
# Prediction Button
# =========================================================
st.write("")

if st.button("🔍 Prediction", width="stretch"):
    st.switch_page("pages/Prediction.py")


# =========================================================
# Developer
# =========================================================

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
