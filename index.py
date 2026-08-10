import streamlit as st



col1,col2,col3,col4=st.columns(4)

with col1:
        if st.button("Home"):
            st.switch_page("index.py")
with col2:
        if st.button("🛡️ Prediction"):
            st.switch_page("pagespredict.py")
with col3:
        if st.button("Model"):
            st.switch_page("pages/model.py")

with col4:
        if st.button("About"):
            st.switch_page("pages/About.py")


with st.container(border=True):

    st.markdown(
        """
    <style>
    .stApp{
    background-color:#eef2f9;
    }
    div.stButton>button{
    background-color:#9CA3AF;
    border:solid;


    }
    my-image{
    width:20px
    }
    </style>

    """,unsafe_allow_html=True)

    col_1,col_2,col_3=st.columns([1,3,1])
    with col_2:
        st.image("imge.jpg",width=500)

    st.markdown("""
                <h2>AI-Based Cyber Attack Detection and Classification System</h2>
            
                """
                ,unsafe_allow_html=True)
    st.markdown("""#### 1.System Overview
        An intelligent system that leverages Machine Learning
        techniques to detect and classify cyber attacks by analyzing network
        traffic data. The system is designed to help cybersecurity
        professionals identify threats quickly and accurately
                """)

    st.markdown("#### 2. Project Objectives")
    st.markdown("""
                
            ###### . Display the objectives inside a card:
                
                - ✅ Detect cyber attacks.
                - ✅ Classify attack types.
                - ✅ Display prediction confidence.
                - ✅ Provide a user-friendly interface.
                - ✅ Improve threat detection and response speed.

                
                """)

    st.markdown(""" #### 3. Model Information:
            - Algorithm :Random Forest
            - Dataset:UNSW-NB15
            - Number of Features : 13 Feature
            - Number of Attack Categories : 10 Categories
    """)


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


