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
#### Evaluate the performance of the Machine Learning model using standard classification metrics

## Model Information
""")

st.markdown("""
                        ### 1.                       🤖 Machine Learning Algorithm
#### Random Forest Classifier:
Random Forest is a supervised Machine Learning algorithm that combines
multiple Decision Trees to make a more accurate and reliable prediction.
#### How Does Random Forest Work?:
.Random Forest creates multiple Decision Trees and trains each tree using 
 a different subset of the training data and features.
            
.Each Decision Tree produces its own prediction, and the final classification
 is determinedby combining the predictions of all trees.
            
.In classification problems, the class that receives the highest number of 
 votes is selected as the final prediction.
            
#### Why Random Forest for Cyber Attack Detection?:
.Random Forest is suitable for cyber attack detection because network 
 traffic contains many features and complex relationships between them.
            
.The algorithm can handle a large number of features and identify important
 patterns in network traffic.
            
.It can also provide good performance for multi-class classification, where
 the system needs to distinguish between normal traffic and different types 
of cyber attacks.
#### Random Forest in This Project:
.In this project, Random Forest is used to analyze network traffic features 
and classify each network connection into one of the predefined categories.

.The model predicts whether the traffic is normal or represents a cyber attack. 
If an attack is detected, the model identifies the attack category.

#### Prediction Process:


     * Network Traffic
         ↓
     * Feature Extraction
         ↓
    * Data Preprocessing 
         ↓
     * Random Forest
         ↓
    * Multiple Decision Trees 
         ↓
    * Voting
         ↓
    * Final Prediction
         ↓
    * Normal / Attack Type
#### Model Configuration:
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
1. Number of Trees: The model uses 150 Decision Trees to produce
the final prediction.
2. Maximum Depth: Each tree can grow up to a maximum depth of 15.
3. Minimum Samples Split: A node must contain at least 4 samples 
before it can be split.
4. Bootstrap: Bootstrap sampling is enabled, allowing each tree to 
be trained using a randomly sampled subset of the training data.    
#### Dataset:
*The UNSW-NB15 dataset is a modern benchmark dataset widely used for 
network intrusion detection systems (NIDS).
*It was generated using an IXIA PerfectStorm tool to capture a hybrid
of real modern normal activities and synthetic contemporary attack
behaviors.
##### Size & Structure: 
It contains approximately 2.5 million records distributed across 45 
features, including class labels.
##### Attack Categories:
It covers nine distinct attack types: Fuzzers, Analysis, Backdoors,
DoS, Exploits, Generic, Reconnaissance, Shellcode, and Worms.
###### Features:
Includes flow features, basic features, content features, time features,
and additional generated features.Purpose: Designed to overcome the
limitations of older datasets, like KDDCUP99, by reflecting realistic,
modern network traffic complexities.
#### Task: Multi-Class Classification
#### Number of Classes: 10
#### Accuracy: 75.40%
Accuracy represents the percentage of all predictions that were correctly classified.
#### Precision: 85.80%
Precision measures how many of the samples predicted as a particular class actually 
belong to that class
#### Precision: 75.80%
Precision measures how many of the samples predicted as a particular class actually belong 
to that class
#### F1-Score: 77.20%
F1-Score provides a balance between Precision and Recall
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

The Confusion Matrix shows the number of correct and incorrect predictions for 
each attack category  

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

   accuracy                            0.75     32549
   macro avg       0.56      0.71      0.59     32549
   weighted avg    0.85      0.75      0.78     32549
Display the following metrics for each attack category:




     
            
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
