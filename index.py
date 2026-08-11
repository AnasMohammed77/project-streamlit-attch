import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Cyber Attack Detection",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------
# Responsive CSS
# --------------------------------------------------
st.markdown("""
<style>

.stApp {
    background-color: #eef2f9;
}

/* Main content */
.block-container {
    padding-top: 2rem;
    padding-left: 5%;
    padding-right: 5%;
}

/* Navigation buttons */
div.stButton > button {
    width: 100%;
    background-color: #9CA3AF;
    color: white;
    border: 1px solid #6B7280;
    border-radius: 10px;
    padding: 8px 5px;
    font-size: 16px;
    font-weight: 600;
    transition: 0.2s;
}

div.stButton > button:hover {
    background-color: #6B7280;
    color: white;
    border-color: #4B5563;
}

/* Main container */
.main-card {
    background-color: white;
    padding: 30px;
    border-radius: 20px;
    margin-top: 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    margin: 20px 0;
}

/* Section title */
.section-title {
    font-size: 24px;
    font-weight: bold;
    margin-top: 25px;
}

/* Statistics table */
.stats-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
    text-align: center;
    overflow: hidden;
    border-radius: 10px;
}

.stats-table th,
.stats-table td {
    padding: 12px;
    border: 1px solid #ddd;
}

.stats-table th {
    background-color: #ff6478;
    color: white;
}

.stats-table tr:nth-child(even) {
    background-color: #f3f4f6;
}

/* Developer card */
.developer-card {
    border: 2px dashed #9CA3AF;
    margin-top: 40px;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    background-color: #f9fafb;
}

.footer {
    margin-top: 20px;
    padding: 10px;
    background-color: #111827;
    color: white;
    text-align: center;
    border-radius: 10px;
}


/* --------------------------------------------------
   Mobile Responsive Design
   -------------------------------------------------- */

@media (max-width: 768px) {

    .block-container {
        padding-left: 3%;
        padding-right: 3%;
        padding-top: 1rem;
    }

    /* Navigation buttons */
    div.stButton > button {
        font-size: 12px;
        padding: 7px 2px;
        border-radius: 8px;
    }

    /* Main card */
    .main-card {
        padding: 15px;
        border-radius: 15px;
    }

    /* Title */
    .main-title {
        font-size: 22px;
        line-height: 1.4;
    }

    /* Section titles */
    .section-title {
        font-size: 19px;
    }

    /* Text */
    .description {
        font-size: 14px;
        line-height: 1.7;
    }

    /* Image */
    .responsive-image img {
        max-width: 100%;
        height: auto;
    }

    /* Table */
    .stats-table {
        font-size: 12px;
    }

    .stats-table th,
    .stats-table td {
        padding: 8px 4px;
    }

    /* Developer */
    .developer-card {
        padding: 15px;
        font-size: 13px;
    }

    .footer {
        font-size: 12px;
    }
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Navigation
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Home", use_container_width=True):
        st.switch_page("index.py")

with col2:
    if st.button("🛡️ Prediction", use_container_width=True):
        st.switch_page("pages/predict.py")

with col3:
    if st.button("Model", use_container_width=True):
        st.switch_page("pages/model.py")

with col4:
    if st.button("About", use_container_width=True):
        st.switch_page("pages/About.py")


# --------------------------------------------------
# Main Content
# --------------------------------------------------

with st.container(border=True):

    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    # Image
    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        st.image(
            "imge.jpg",
            use_container_width=True
        )

    # Title
    st.markdown(
        """
        <div class="main-title">
            AI-Based Cyber Attack Detection and Classification System
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------
    # System Overview
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">1. System Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="description">
        An intelligent system that leverages Machine Learning
        techniques to detect and classify cyber attacks by analyzing
        network traffic data. The system is designed to help
        cybersecurity professionals identify threats quickly and
        accurately.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------
    # Objectives
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">2. Project Objectives</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="description">

        - ✅ Detect cyber attacks.
        - ✅ Classify attack types.
        - ✅ Display prediction confidence.
        - ✅ Provide a user-friendly interface.
        - ✅ Improve threat detection and response speed.

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------
    # Model Information
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">3. Model Information</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="description">

        - 🤖 <b>Algorithm:</b> Random Forest
        - 📊 <b>Dataset:</b> UNSW-NB15
        - 🔢 <b>Number of Features:</b> 13 Features
        - 🛡️ <b>Number of Attack Categories:</b> 10 Categories

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------
    # Quick Statistics
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">4. Quick Statistics</div>',
        unsafe_allow_html=True
    )

st.markdown(""" 
  
                <h2> 4. Quick Statistics (Dashboard)</h2>
  
                
  
                <table style="background-color:silver;text-algin:center;margin:0px 50px;width:80%">
  
                <tr style="background-color:rgb(255,100,120)">
  
                <th>Metric</th>            <th>Value</th>
  
                </tr>
  

  
                <tr>
  
                <td>📂 Total Samples</td>            <td>257,673</td>
  
                </tr>
  

  
                <tr>
  
                <td>🛡️ Attack Categories</td>            <td>10</td>
  
                </tr>
  

  
                <tr>
  
                <td> 🎯 Model Accuracy</td>            <td>75.9%</td>
  
                </tr>
  
                
  
                <tr>
  
                <td> ⚡️ Prediction Time </td>            <td>0.03 sec</td>
  
                </tr>
  
                </table>
  
                
  
            
  

  
    """ ,unsafe_allow_html=True)
  
        
  

    # --------------------------------------------------
    # Developer
    # --------------------------------------------------

    st.markdown(
        """
        <div class="developer-card">

            <h4>Developed by:</h4>

            <b>Student: Anas Mohammed Abd Alijalyl Saeed</b>

            <p>
                Department of Artificial Intelligence<br>
                University of Taiz
            </p>

            <div class="footer">
                © 2026
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)
