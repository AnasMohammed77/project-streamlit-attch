import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Model Information",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

    /* ==============================
       Main Page
       ============================== */

    .block-container {
    background-color: #F5F5F5;
        max-width: 1400px;
        padding: 2rem 5%;
        margin: auto;
    }


    /* ==============================
       Navigation Buttons
       ============================== */

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


    /* ==============================
       Page Title
       ============================== */

    .page-title {
        text-align: center;
        background-color: cyan;
        padding: 12px;
        border-radius: 30px;
        margin: 25px 0;
        color: black;
    }


    /* ==============================
       Cards
       ============================== */

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 25px;
        margin: 15px 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
        font-size: 16px;
        line-height: 1.7;
    }

    .card h3 {
        color: #2563EB;
        margin-top: 5px;
    }

    .card h4 {
        color: #374151;
        margin-top: 20px;
    }


    /* ==============================
       Section Title
       ============================== */

    .section-title {
        color: #2563EB;
        border-left: 5px solid #2563EB;
        padding-left: 12px;
        margin-top: 10px;
    }


    /* ==============================
       Metric Cards
       ============================== */

    .metric-card {
        background-color: white;
        padding: 20px;
        text-align: center;
        border-radius: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        margin: 10px 0;
    }

    .metric-title {
        font-size: 17px;
        font-weight: bold;
        color: #374151;
    }

    .metric-value {
        font-size: 30px;
        font-weight: bold;
        color: #2563EB;
        margin-top: 5px;
    }


    /* ==============================
       Prediction Process
       ============================== */

    .process {
        text-align: center;
        background-color: #F5F5F5;
        padding: 20px;
        border-radius: 20px;
        font-size: 18px;
        font-weight: bold;
        line-height: 2;
    }

    .process-step {
        background-color: white;
        padding: 10px;
        margin: 5px auto;
        border-radius: 12px;
        max-width: 500px;
        box-shadow: 0 1px 5px rgba(0,0,0,0.08);
    }


    /* ==============================
       Contact
       ============================== */

    .contact {
        text-align: center;
        border: 2px dashed #555;
        padding: 20px;
        border-radius: 25px;
        margin-top: 35px;
    }

    .contact h2 {
        background-color: cyan;
        padding: 10px;
        border-radius: 25px;
    }

    .contact a {
        display: block;
        max-width: 400px;
        margin: 10px auto;
        padding: 10px;
        background-color: cyan;
        color: black;
        text-decoration: none;
        border-radius: 50px;
    }

    .contact a:hover {
        background-color: #00BFBF;
    }


    /* ==============================
       Developer
       ============================== */

    .developer {
        text-align: center;
        background-color: white;
        border: 2px dashed #555;
        padding: 20px;
        margin: 40px 0;
        border-radius: 30px;
    }

    .copyright {
        background-color: black;
        color: white;
        padding: 8px;
        border-radius: 10px;
        margin-top: 15px;
    }


    /* ==============================
       Mobile
       ============================== */

    @media (max-width: 600px) {

        .block-container {
            padding-left: 15px;
            padding-right: 15px;
            padding-top: 1rem;
        }

        .page-title {
            font-size: 23px;
        }

        .card {
            padding: 15px;
            font-size: 15px;
        }

        .metric-value {
            font-size: 25px;
        }

        .process {
            font-size: 15px;
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
# Page Title
# =========================================================

st.markdown("""
<h2 class="page-title">
    🤖 Model Information & Performance
</h2>
""", unsafe_allow_html=True)


# =========================================================
# Image
# =========================================================

col1, col2, col3 = st.columns([1, 5, 1])

with col2:
    st.image(
        "imge.jpg",
        use_container_width=True
    )


st.markdown("""
<p style="text-align:center; font-size:18px; color:#555;">
Evaluate the performance of the Machine Learning model using
standard classification metrics.
</p>
""", unsafe_allow_html=True)


# =========================================================
# 1. Machine Learning Algorithm
# =========================================================

st.markdown("""
<div class="card">

<h3 class="section-title">
1. 🤖 Machine Learning Algorithm
</h3>

<h4>1.1 Random Forest Classifier</h4>

<p>
Random Forest is a supervised Machine Learning algorithm that combines
multiple Decision Trees to produce more accurate and reliable predictions.
</p>

<p>
The algorithm creates multiple Decision Trees and trains each tree using
different subsets of the training data and features.
</p>

<p>
Each Decision Tree produces its own prediction, and the final classification
is determined by combining the predictions of all trees.
</p>

<p>
In classification problems, the class that receives the highest number
of votes is selected as the final prediction.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 1.2 Why Random Forest
# =========================================================

st.markdown("""
<div class="card">

<h4>1.2 Why Random Forest for Cyber Attack Detection?</h4>

<p>
Random Forest is suitable for cyber attack detection because network traffic
contains many features and complex relationships between them.
</p>

<p>
The algorithm can handle a large number of features and identify important
patterns in network traffic.
</p>

<p>
It can also provide good performance for multi-class classification, where
the system needs to distinguish between normal traffic and different types
of cyber attacks.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 1.3 Random Forest in This Project
# =========================================================

st.markdown("""
<div class="card">

<h4>1.3 Random Forest in This Project</h4>

<p>
In this project, Random Forest is used to analyze network traffic features
and classify each network connection into one of the predefined categories.
</p>

<p>
The model predicts whether the traffic is normal or represents a cyber attack.
If an attack is detected, the model identifies the corresponding attack category.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 2. Prediction Process
# =========================================================

st.markdown("""
<div class="card">

<h3 class="section-title">
2. 🔄 Prediction Process
</h3>

<div class="process">

<div class="process-step">
🌐 Network Traffic
</div>

↓

<div class="process-step">
📌 Feature Extraction
</div>

↓

<div class="process-step">
⚙️ Data Preprocessing
</div>

↓

<div class="process-step">
🌲 Random Forest
</div>

↓

<div class="process-step">
🌳 150 Decision Trees
</div>

↓

<div class="process-step">
🗳️ Majority Voting
</div>

↓

<div class="process-step">
🎯 Final Prediction
</div>

↓

<div class="process-step">
🛡️ Normal / Attack Type
</div>

</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 2.1 Model Configuration
# =========================================================

st.markdown("""
<div class="card">

<h3 class="section-title">
2.1 ⚙️ Model Configuration
</h3>

</div>
""", unsafe_allow_html=True)


config_data = {
    "Parameter": [
        "Algorithm",
        "Number of Trees",
        "Maximum Depth",
        "Minimum Samples Split",
        "Bootstrap",
        "Random State",
        "Classification Type",
        "Class Weight"
    ],

    "Value": [
        "Random Forest",
        "150",
        "15",
        "4",
        "True",
        "42",
        "Multi-Class",
        "Balanced"
    ]
}

config_df = pd.DataFrame(config_data)

st.dataframe(
    config_df,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# Model Parameters Explanation
# =========================================================

st.markdown("""
<div class="card">

<h4>1. Number of Trees</h4>

<p>
The model uses <b>150 Decision Trees</b> to produce the final prediction.
</p>

<h4>2. Maximum Depth</h4>

<p>
Each tree can grow up to a maximum depth of <b>15</b>.
</p>

<h4>3. Minimum Samples Split</h4>

<p>
A node must contain at least <b>4 samples</b> before it can be split.
</p>

<h4>4. Bootstrap</h4>

<p>
Bootstrap sampling is enabled, allowing each tree to be trained using
a randomly sampled subset of the training data.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 3. Dataset
# =========================================================

st.markdown("""
<div class="card">

<h3 class="section-title">
3. 🗂️ Dataset
</h3>

<p>
The <b>UNSW-NB15</b> dataset is a benchmark dataset widely used for
network intrusion detection systems (NIDS).
</p>

<p>
It contains normal network activities and different types of
contemporary cyber attack behaviors.
</p>

<h4>Dataset Characteristics</h4>

<ul>
    <li><b>Dataset:</b> UNSW-NB15</li>
    <li><b>Task:</b> Multi-Class Classification</li>
    <li><b>Number of Classes:</b> 10</li>
</ul>

</div>
""", unsafe_allow_html=True)


# =========================================================
# Attack Categories
# =========================================================

attack_categories = [
    "Normal",
    "Fuzzers",
    "Analysis",
    "Backdoors",
    "DoS",
    "Exploits",
    "Generic",
    "Reconnaissance",
    "Shellcode",
    "Worms"
]

st.markdown("""
<div class="card">

<h4>3.1 Attack Categories</h4>

</div>
""", unsafe_allow_html=True)

attack_df = pd.DataFrame({
    "Class": range(10),
    "Category": attack_categories
})

st.dataframe(
    attack_df,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# Features
# =========================================================

st.markdown("""
<div class="card">

<h4>3.2 Features</h4>

<p>
The dataset includes different types of network traffic features,
including flow features, basic features, content features,
time-related features, and additional generated features.
</p>

<p>
These features help the Machine Learning model identify patterns
associated with normal and malicious network traffic.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 4. Model Performance
# =========================================================

st.markdown("""
<h3 class="section-title">
4. 📈 Model Performance
</h3>
""", unsafe_allow_html=True)


# =========================================================
# Metrics
# =========================================================

metric1, metric2, metric3, metric4 = st.columns(4)


with metric1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Accuracy</div>
        <div class="metric-value">75.40%</div>
    </div>
    """, unsafe_allow_html=True)


with metric2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Precision</div>
        <div class="metric-value">85.80%</div>
    </div>
    """, unsafe_allow_html=True)


with metric3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Recall</div>
        <div class="metric-value">75.80%</div>
    </div>
    """, unsafe_allow_html=True)


with metric4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">F1-Score</div>
        <div class="metric-value">77.20%</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# Metrics Explanation
# =========================================================

st.markdown("""
<div class="card">

<h4>Accuracy</h4>

<p>
Accuracy represents the percentage of all predictions that were
correctly classified.
</p>

<h4>Precision</h4>

<p>
Precision measures how many of the samples predicted as a particular
class actually belong to that class.
</p>

<h4>Recall</h4>

<p>
Recall measures how many of the actual samples belonging to a class
were correctly identified by the model.
</p>

<h4>F1-Score</h4>

<p>
F1-Score provides a balance between Precision and Recall.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 5. Confusion Matrix
# =========================================================

st.markdown("""
<div class="card">

<h3 class="section-title">
5. 🔥 Confusion Matrix
</h3>

<p>
The Confusion Matrix shows the number of correct and incorrect
predictions for each attack category.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# Confusion Matrix Data
# =========================================================

matrix = [
    [294, 113, 14, 3, 0, 0, 2, 0, 2, 0],
    [230, 83, 15, 2, 3, 2, 0, 4, 12, 1],
    [235, 104, 372, 248, 17, 10, 2, 29, 58, 0],
    [259, 104, 289, 4206, 125, 31, 3, 364, 132, 34],
    [227, 110, 14, 45, 3623, 5, 35, 5, 80, 0],
    [55, 9, 24, 72, 15, 1351, 0, 1, 3, 4],
    [556, 7, 71, 162, 3759, 2, 12425, 12, 117, 1],
    [191, 61, 9, 27, 6, 1, 0, 1717, 23, 5],
    [1, 1, 0, 0, 22, 0, 0, 1, 259, 0],
    [0, 0, 0, 5, 0, 0, 0, 1, 0, 27]
]


# =========================================================
# Heatmap
# =========================================================

fig, ax = plt.subplots(figsize=(10, 7))

sns.heatmap(
    matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=attack_categories,
    yticklabels=attack_categories,
    ax=ax
)

ax.set_xlabel("Predicted Class")
ax.set_ylabel("Actual Class")
ax.set_title("Confusion Matrix")

plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)

st.pyplot(fig, use_container_width=True)

plt.close(fig)


# =========================================================
# 6. Classification Report
# =========================================================

st.markdown("""
<div class="card">

<h3 class="section-title">
6. 📋 Classification Report
</h3>

<p>
The Classification Report provides Precision, Recall, F1-Score,
and Support for each attack category.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# Classification Report Data
# =========================================================

report_data = {
    "Class": [
        "0", "1", "2", "3", "4",
        "5", "6", "7", "8", "9"
    ],

    "Precision": [
        0.14, 0.14, 0.46, 0.88, 0.48,
        0.96, 1.00, 0.80, 0.38, 0.38
    ],

    "Recall": [
        0.69, 0.24, 0.35, 0.76, 0.87,
        0.88, 0.73, 0.84, 0.91, 0.82
    ],

    "F1-Score": [
        0.24, 0.18, 0.40, 0.82, 0.62,
        0.92, 0.84, 0.82, 0.53, 0.51
    ],

    "Support": [
        428, 352, 1075, 5547, 4144,
        1534, 17112, 2040, 284, 33
    ]
}


report_df = pd.DataFrame(report_data)

report_df["Category"] = attack_categories

report_df = report_df[
    [
        "Class",
        "Category",
        "Precision",
        "Recall",
        "F1-Score",
        "Support"
    ]
]


st.dataframe(
    report_df,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# Conclusion
# =========================================================

st.markdown("""
<div class="card">

<h3 class="section-title">
7. 📝 Conclusion
</h3>

<p>
The Random Forest model provides a practical approach for
multi-class cyber attack detection. The model analyzes network
traffic features and classifies network connections into normal
traffic or different cyber attack categories.
</p>

<p>
The evaluation results show that the model can successfully
identify several attack categories while the Confusion Matrix
and Classification Report provide detailed information about
the strengths and weaknesses of the classification performance.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# Contact
# =========================================================

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
        💬 Messenger
    </a>

<a href="https://www.facebook.com/share/19Fw8BRK99/">
        👍 Facebook
    </a>

<a href="https://t.me/Anas_Alsanwy" target="_blank">
        ✈️ Telegram
    </a>
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
