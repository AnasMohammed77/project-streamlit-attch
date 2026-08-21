import streamlit as st

st.set_page_config(
    page_title="AI Project",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

    /* إزالة المساحات الزائدة */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 5%;
        padding-right: 5%;
        max-width: 1400px;
        margin: auto;
    }

    /* الأزرار */
    .stButton > button {
        width: 100%;
        min-height: 45px;
        border-radius: 10px;
        font-size: 16px;
    }

    /* البطاقات */
    .card {
        width: 100%;
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        box-sizing: border-box;
    }

    /* الصور */
    img {
        max-width: 100%;
        height: auto;
    }

    /* الشاشات المتوسطة */
    @media (max-width: 900px) {

        .block-container {
            padding-left: 3%;
            padding-right: 3%;
        }

        .card {
            padding: 16px;
        }

    }

    /* الجوال */
    @media (max-width: 600px) {

        .block-container {
            padding-left: 15px;
            padding-right: 15px;
            padding-top: 1rem;
        }

        .card {
            padding: 14px;
            border-radius: 12px;
        }

        .stButton > button {
            min-height: 42px;
            font-size: 14px;
        }

        h1 {
            font-size: 2px !important;
        }

        h2 {
            font-size: 2px !important;
        }

        h3 {
            font-size: 1px !important;
        }

    }

</style>
""", unsafe_allow_html=True)
st.markdown(
        """
    <style>
div.stButton>button{
background-color:limegreen;
border:non ;
}
    my-image{
    width:20px
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
<h2 style="border-radius:30px;text-align:center;background:cyan"> Model Information</h2>

""",unsafe_allow_html=True)
col_1,col_2,col_3=st.columns([1,5,1])
with col_2:
        st.image("imge.jpg")


        st.markdown("""
        #### Evaluate the performance of the Machine Learning model using standard classification metrics

        """)

        st.markdown("""    
        <div style="background:#9CA3AF;font-size:20px;padding:20px;border-radius:25px;">
        <div style="background:white;font-size:1px;padding:20px;border-radius:25px;margin:10px 0">
                <h5 style="color:blue;">1.🤖 Machine Learning Algorithm<h5>
                <h6>1.1 Random Forest Classifier:<h5>
        <i style="font-size:10px;">

        <p>
                        Random Forest is a supervised Machine Learning algorithm that combines
                multiple Decision Trees to make a more accurate and reliable prediction.
        </p>
        <p>       
                .Random Forest creates multiple Decision Trees and trains each tree using 
                a different subset of the training data and features.</p>
        <p>      
                .Each Decision Tree produces its own prediction, and the final classification
                is determinedby combining the predictions of all trees.</p>
        <p>      
                .In classification problems, the class that receives the highest number of 
                votes is selected as the final prediction.
        </p>
        </i>
        </div>
        <div style="background:white;font-size:20px;padding:20px;border-radius:25px">
                <h6>1.2 Why Random Forest for Cyber Attack Detection?:<h6>
        <i style="font-size:10px;">

        <p>
                .Random Forest is suitable for cyber attack detection because network 
                        traffic contains many features and complex relationships between them.
        </p>
        <p>
        .The algorithm can handle a large number of features and identify important
                patterns in network traffic.
        </p>
        <p>      
                .It can also provide good performance for multi-class classification, where
                        the system needs to distinguish between normal traffic and different types 
                        of cyber attacks.
        </p>


        </i>     
        </div>
                
                
        <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">
                <h3>1.3 Random Forest in This Project:<h3>
        <i style="font-size:10px;">

        <p>
                .In this project, Random Forest is used to analyze network traffic features 
                and classify each network connection into one of the predefined categories.
        </p>
        <p>
                .The model predicts whether the traffic is normal or represents a cyber attack. 
                If an attack is detected, the model identifies the attack category.
        </p>
        </i>
        </div>

        <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">
        <h6 style="color:blue">2. Prediction Process:</h5>



     * Network traffic                       ↓
     * Feature Extraction
              ↓
     * Data Preprocessing
              ↓
       * Random Forest
                                        ↓
       * Multiple Decision Tree
             ↓
       * Votive 
             ↓
      * Final Prediction
             ↓
      * Normal / Attack Type
        </div>
        <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">

        ### 2.1 Model Configuration:
                ______________________________________________
                | Parameter             | Value              |
                |_______________________|____________________|
                | Algorithm             | Random Forest      |
                | Number of Trees       | 150                |
                | Maximum Depth         | 15                 |
                | Minimum Samples Split | 4                  |
                | Bootstrap             | True               |
                | Random State          | 42                 |
                | Classification Type   | Multi-Class        |
                | class_weight          | balanced           |
                |_______________________|____________________|
        <i style="font-size:10px;">
        <h5>        1. Number of Trees:</h5>
        <p>
                The model uses 150 Decision Trees to producethe final prediction.
        <p/>
        <h5>       2. Maximum Depth:</h5>
        <p>
                Each tree can grow up to a maximum depth of 15.
        </p>
        <h5>      3. Minimum Samples Split: </h5>
        <p>
                        A node must contain at least 4 samples before it can be split.
        </p>
        <h5>        4. Bootstrap: </h5>
        <p>
        Bootstrap sampling is enabled, allowing each tree to be trained
        using a randomly sampled subset of the training data. 
        </p>   
        </i>
        </div>
        <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">
        <i style="font-size:10px;">
        <h2 style="color:blue">3. Dataset:</h2>
        <p>
                The UNSW-NB15 dataset is a modern benchmark dataset widely used for 
                network intrusion detection systems (NIDS).
        </p>
        <p>
                It was generated using an IXIA PerfectStorm tool to capture a hybrid
                of real modern normal activities and synthetic contemporary attack
                behaviors.
        </p>
        </i>
        </div>
        <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">

        <h3>3.1 Size & Structure: </h3>
        <p>
                It contains approximately 2.5 million records distributed across 45 
                features, including class labels.
        </p>
        <h3>3.2 Attack Categories</h3>
        <p>
                It covers nine distinct attack types: Fuzzers, Analysis, Backdoors,
                DoS, Exploits, Generic, Reconnaissance, Shellcode, and Worms.
        </p>
        </div>
        <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">
        <i style="font-size:10px;">
        <h3>3.3 Features:</h3>
        <p>
                Includes flow features, basic features, content features, time features,
                and additional generated features.Purpose: Designed to overcome the
                limitations of older datasets, like KDDCUP99, by reflecting realistic,
                modern network traffic complexities.
        </p>
        </div>
        <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">

        <h3> Task: Multi-Class Classification</h3>
        <h3> Number of Classes: 10</h3>
        <h3> Accuracy: 75.40%</h3>
        <p>
        Accuracy represents the percentage of all predictions that were correctly classified.
        </p>
        <h3> Precision: 85.80%</h3>
        <p>
        Precision measures how many of the samples predicted as a particular class actually 
        belong to that class
        </p>
        <h3> Precision: 75.80%</h3>
        <p> Precision measures how many of the samples predicted as a particular class actually belong 
        to that class
        </p>
        <h3>  F1-Score: 77.20%</h3>
        <p> F1-Score provides a balance between Precision and Recall</p>
        </i>
        </div>
        <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">

        #### Confusion Matrix:
                                Confusion Matrix:
                [[  294   113    14     3     0     0     2     0     2     0]
                [  230    83    15     2     3     2     0     4    12     1]
                [  235   104   372   248    17    10     2    29    58     0]
                [  259   104   289  4206   125    31     3   364   132    34]
                [  227   110    14    45  3623     5    35     5    80     0]
                [   55     9    24    72    15  1351     0     1     3     4]
                [  556     7    71   162  3759     2 12425    12   117     1]
                [  191    61     9    27     6     1     0  1717    23     5]
                [    1     1     0     0    22     0     0     1   259     0]
                [    0     0     0     5     0     0     0     1     0    27]]

        <i style="font-size:10px;">
        <p>
                The Confusion Matrix shows the number of correct and incorrect predictions for 
                each attack category  
        </p>
        </div>
        <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">

        #### Classification Report:
                        precision    recall  f1-score   support

                0       0.14      0.69      0.24       428
                1       0.14      0.24      0.18       352
                2       0.46      0.35      0.40      1075
                3       0.88      0.76      0.82      5547
                4       0.48      0.87      0.62      4144
                5       0.96      0.88      0.92      1534
                6       1.00      0.73      0.84     17112
                7       0.80      0.84      0.82      2040
                8       0.38      0.91      0.53       284
                9       0.38      0.82      0.51        33

                accuracy                        0.75     32549
                macro avg       0.56      0.71      0.59     32549
                weighted avg    0.85      0.75      0.78     32549
        Display the following metrics for each attack category:
        </div>
                <div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">
        <div style="text-align:center;border-radius:10px;border:2px dashed;">
        <h2 style="background:#00ffff;border-radius:25px;">Contact Me</h2>
                        <p style="border-radius:70px;background:#00ffff;text-decoration:none;margin:5px 250px"><a href="https://mailto:alsnwyansmhmdbdaljlyl@gmail.com"> @Emial.com</a></p>
                        <p style="border-radius:50px;background:#00ffff;text-decoration:none;margin:5px 250px"><i class="fa-brands fa-whatsapp"></i></i><a href="https://wa.me/967776713367">WhatsApp</a></a></p>
                        <p style="border-radius:50px;background:#00ffff;text-decoration:none;margin:5px 250px"><i class="fa-brands fa-facebook-messenger"></i> <a href="https://m.me/ans.mhmd.alsnwy">Messenger</a></p>
                        <p style="border-radius:50px;background:#00ffff;text-decoration:none;margin:5px 250px"><i class="fa-brands fa-facebook-f"></i><a href="https://www.facebook.com/share/19Fw8BRK99/">Facebook</a></p>
                        <p style="border-radius:50px;background:#00ffff;text-decoration:none;margin:5px 250px"><i class="fab fa-telegram"></i> <a href="https://t.me/Anas_Alsanwy" target="_blank">Telegram</a></p>
        </div> 
        </i>
        </div>   

        </div>


        
                
                """,unsafe_allow_html=True)
        st.write("")
        if st.button("🔍 Prediction",width="stretch"):
                st.switch_page("pages/Prediction.py")

                
        

        matrix=[[294  , 113,    14 ,    3  ,   0 ,    0  ,   2 ,    0 ,    2 ,    0],
                [230 ,   83  ,  15,     2  ,   3 ,    2   ,  0 ,    4  ,  12  ,   1],
                [235  , 104  , 372 ,  248   , 17  ,  10    , 2   , 29  ,  58    , 0],
                [259   ,104  , 289 , 4206  , 125   , 31 ,    3   ,364 ,  132   , 34],
                [  227 ,  110 ,   14   , 45, 3623  ,   5  ,  35  ,   5 ,   80   ,  0],
                [   55  ,   9  ,  24  ,  72  ,  15 , 1351  ,   0  ,   1   ,  3  ,   4],
                [  556  ,   7  ,  71  , 162 , 3759  ,   2, 12425  ,  12 ,  117  ,   1],
                [  191  ,  61   ,  9   , 27    , 6  ,   1   ,  0  ,1717 ,   23  ,   5],
                [    1   ,  1   ,  0   ,  0 ,   22  ,   0   ,  0   ,  1 ,  259   ,  0],
                [    0   ,  0  ,   0   ,  5 ,    0  ,   0   ,  0   ,  1 ,    0  ,  27]]
        # data=pd.DataFrame(matrix)
        # fig,ax=plt.subplots()
        # sns.heatmap(matrix,cmap="Accent_r")
        # st.pyplot(fig)
        # plt.show()
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
