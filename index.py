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
# CSS - Responsive Design
# =========================================================

st.markdown("""
<style>

/* ------------------------------
   Main application background
------------------------------ */

.stApp {
    background-color: #eef2f9;
}


/* ------------------------------
   Main content width
------------------------------ */

.block-container {
    padding-top: 1.5rem;
    padding-left: 5%;
    padding-right: 5%;
}


/* ------------------------------
   Navigation buttons
------------------------------ */

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


/* Button hover */

div.stButton > button:hover {

    background-color: #6B7280;

    color: white;

    border-color: #4B5563;
}


/* ------------------------------
   Main container
------------------------------ */

.main-content {

    background-color: white;

    padding: 30px;

    border-radius: 20px;

    margin-top: 20px;

    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}


/* ------------------------------
   Main title
------------------------------ */

.main-title {

    text-align: center;

    font-size: 32px;

    font-weight: bold;

    margin: 20px 0;

    line-height: 1.4;
}


/* ------------------------------
   Section titles
------------------------------ */

.section-title {

    font-size: 23px;

    font-weight: bold;

    margin-top: 25px;

    margin-bottom: 10px;
}


/* ------------------------------
   Description
------------------------------ */

.description {

    font-size: 16px;

    line-height: 1.8;

    color: #374151;
}


/* ------------------------------
   Statistics table
------------------------------ */

.stats-table {

    width: 100%;

    border-collapse: collapse;

    text-align: center;

    margin-top: 15px;

    background-color: white;

    border-radius: 10px;

    overflow: hidden;
}


.stats-table th {

    background-color: rgb(255,100,120);

    color: white;

    padding: 12px;

    border: 1px solid #ddd;
}


.stats-table td {

    padding: 12px;

    border: 1px solid #ddd;

    color: #222;
}


.stats-table tr:nth-child(even) {

    background-color: #f3f4f6;
}


/* ------------------------------
   Developer card
------------------------------ */

.developer-card {

    border: 2px dashed #9CA3AF;

    margin-top: 40px;

    padding: 20px;

    border-radius: 30px;

    text-align: center;

    background-color: #f9fafb;
}


.footer {

    margin-top: 20px;

    padding: 10px;

    border-radius: 8px;

    background-color: black;

    color: white;

    text-align: center;
}


/* =========================================================
   Mobile
========================================================= */

@media (max-width: 768px) {


    /* Page spacing */

    .block-container {

        padding-left: 3%;

        padding-right: 3%;

        padding-top: 1rem;
    }


    /* Navigation */

    div.stButton > button {

        font-size: 11px;

        padding: 7px 2px;

        border-radius: 7px;
    }


    /* Main content */

    .main-content {

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

        font-size: 19px;
    }


    /* Description */

    .description {

        font-size: 14px;

        line-height: 1.7;
    }


    /* Statistics table */

    .stats-table {

        font-size: 12px;

        width: 100%;
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


    /* Footer */

    .footer {

        font-size: 12px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# Navigation
# =========================================================

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


# =========================================================
# Main Content
# =========================================================

with st.container(border=True):

    st.markdown(
        '<div class="main-content">',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # Image
    # -----------------------------------------------------

    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:

        st.image(
            "imge.jpg",
            use_container_width=True
        )


    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------

    st.markdown(
        """
        <div class="main-title">
            AI-Based Cyber Attack Detection and Classification System
        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # 1. System Overview
    # =====================================================

    st.markdown(
        """
        <div class="section-title">
            1. System Overview
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="description">

        An intelligent system that leverages Machine Learning
        techniques to detect and classify cyber attacks by analyzing
        network traffic data. The system is designed to help
        cybersecurity professionals identify threats quickly
        and accurately.

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # 2. Project Objectives
    # =====================================================

    st.markdown(
        """
        <div class="section-title">
            2. Project Objectives
        </div>
        """,
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


    # =====================================================
    # 3. Model Information
    # =====================================================

    st.markdown(
        """
        <div class="section-title">
            3. Model Information
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="description">

        - 🤖 <b>Algorithm:</b> Random Forest
        <br>
        - 📊 <b>Dataset:</b> UNSW-NB15
        <br>
        - 🔢 <b>Number of Features:</b> 13 Features
        <br>
        - 🛡️ <b>Number of Attack Categories:</b> 10 Categories

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # 4. Quick Statistics
    # =====================================================

    st.markdown(
        """
        <div class="section-title">
            4. Quick Statistics (Dashboard)
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <table class="stats-table">

            <tr>

                <th>
                    Metric
                </th>

                <th>
                    Value
                </th>

            </tr>


            <tr>

                <td>
                    📂 Total Samples
                </td>

                <td>
                    257,673
                </td>

            </tr>


            <tr>

                <td>
                    🛡️ Attack Categories
                </td>

                <td>
                    10
                </td>

            </tr>


            <tr>

                <td>
                    🎯 Model Accuracy
                </td>

                <td>
                    75.9%
                </td>

            </tr>


            <tr>

                <td>
                    ⚡ Prediction Time
                </td>

                <td>
                    0.03 sec
                </td>

            </tr>

        </table>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # Developer
    # =====================================================

    st.markdown(
        """
        <div class="developer-card">

            <h4>
                Developed by:
            </h4>

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


    st.markdown(
        '</div>',
        unsafe_allow_html=True
)
