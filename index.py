import streamlit as st


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Cyber Attack Detection",
    page_icon="🛡️",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   Page Background
===================================================== */

.stApp {
    background-color: #eef2f9;
}


/* =====================================================
   Navigation
===================================================== */

.nav-container {
    background-color: white;
    padding: 12px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}


/* Navigation buttons */

div.stButton > button {

    width: 100%;

    background-color: #9CA3AF;

    color: white;

    border: 1px solid #6B7280;

    border-radius: 10px;

    padding: 8px 5px;

    font-size: 15px;

    font-weight: 600;
}


/* Hover */

div.stButton > button:hover {

    background-color: #6B7280;

    color: white;

    border-color: #4B5563;
}


/* =====================================================
   Cards
===================================================== */

.card {

    background-color: white;

    padding: 25px;

    border-radius: 18px;

    margin-top: 20px;

    margin-bottom: 20px;

    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);

    border: 1px solid #e5e7eb;
}


/* =====================================================
   Main Title
===================================================== */

.main-title {

    text-align: center;

    font-size: 30px;

    font-weight: bold;

    color: #1f2937;

    margin-top: 10px;

    margin-bottom: 20px;
}


/* =====================================================
   Section Titles
===================================================== */

.section-title {

    font-size: 22px;

    font-weight: bold;

    color: #1f2937;

    margin-bottom: 10px;
}


/* =====================================================
   Text
===================================================== */

.card-text {

    font-size: 16px;

    line-height: 1.8;

    color: #374151;
}


/* =====================================================
   Statistics Table
===================================================== */

.stats-table {

    width: 100%;

    border-collapse: collapse;

    text-align: center;

    margin-top: 15px;
}


.stats-table th {

    background-color: #ff6478;

    color: white;

    padding: 12px;

    border: 1px solid #ddd;
}


.stats-table td {

    padding: 12px;

    border: 1px solid #ddd;

    color: #374151;
}


.stats-table tr:nth-child(even) {

    background-color: #f3f4f6;
}


/* =====================================================
   Developer Card
===================================================== */

.developer-card {

    background-color: white;

    padding: 25px;

    border: 2px dashed #9CA3AF;

    border-radius: 20px;

    text-align: center;

    margin-top: 25px;
}


.footer {

    background-color: #111827;

    color: white;

    padding: 10px;

    border-radius: 8px;

    margin-top: 15px;
}


/* =====================================================
   Mobile Responsive
===================================================== */

@media (max-width: 768px) {

    /* Navigation */

    div.stButton > button {

        font-size: 11px;

        padding: 7px 2px;

        border-radius: 7px;
    }


    /* Cards */

    .card {

        padding: 15px;

        border-radius: 15px;
    }


    /* Main title */

    .main-title {

        font-size: 21px;

        line-height: 1.5;
    }


    /* Section title */

    .section-title {

        font-size: 18px;
    }


    /* Text */

    .card-text {

        font-size: 14px;

        line-height: 1.7;
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

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# Navigation Bar
# =========================================================

st.markdown(
    '<div class="nav-container">',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    if st.button(
        "Home",
        use_container_width=True
    ):

        st.switch_page("index.py")


with col2:

    if st.button(
        "🛡️ Prediction",
        use_container_width=True
    ):

        st.switch_page("pages/predict.py")


with col3:

    if st.button(
        "Model",
        use_container_width=True
    ):

        st.switch_page("pages/model.py")


with col4:

    if st.button(
        "About",
        use_container_width=True
    ):

        st.switch_page("pages/About.py")


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# Main Image Card
# =========================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns([1, 3, 1])

with col2:

    st.image(
        "imge.jpg",
        use_container_width=True
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# Main Title
# =========================================================

st.markdown(
    """
    <div class="card">

        <div class="main-title">
            AI-Based Cyber Attack Detection and Classification System
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 1. System Overview
# =========================================================

st.markdown(
    """
    <div class="card">

        <div class="section-title">
            1. System Overview
        </div>

        <div class="card-text">

        An intelligent system that leverages Machine Learning
        techniques to detect and classify cyber attacks by analyzing
        network traffic data.

        The system is designed to help cybersecurity professionals
        identify threats quickly and accurately.

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 2. Project Objectives
# =========================================================

st.markdown(
    """
    <div class="card">

        <div class="section-title">
            2. Project Objectives
        </div>

        <div class="card-text">

        <p>🎯 The main objectives of the system are:</p>

        <ul>

            <li>✅ Detect cyber attacks.</li>

            <li>✅ Classify attack types.</li>

            <li>✅ Display prediction confidence.</li>

            <li>✅ Provide a user-friendly interface.</li>

            <li>✅ Improve threat detection and response speed.</li>

        </ul>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 3. Model Information
# =========================================================

st.markdown(
    """
    <div class="card">

        <div class="section-title">
            3. Model Information
        </div>

        <div class="card-text">

        <p>🤖 <b>Algorithm:</b> Random Forest</p>

        <p>📊 <b>Dataset:</b> UNSW-NB15</p>

        <p>🔢 <b>Number of Features:</b> 13 Features</p>

        <p>🛡️ <b>Number of Attack Categories:</b> 10 Categories</p>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. Quick Statistics
# =========================================================

st.markdown(
    """
    <div class="card">

        <div class="section-title">
            4. Quick Statistics (Dashboard)
        </div>

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

                <td>75.9%</td>

            </tr>


            <tr>

                <td>⚡ Prediction Time</td>

                <td>0.03 sec</td>

            </tr>

        </table>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Developer
# =========================================================

st.markdown(
    """
    <div class="developer-card">

        <h3>
            Developed by
        </h3>

        <b>
            Student: Anas Mohammed Abd ALijalyl Saeed
        </b>

        <p>
            Department of Artificial Intelligence
            <br>
            University of Taiz
        </p>


        <div class="footer">

            © 2026

        </div>

    </div>
    """,
    unsafe_allow_html=True
)
