import streamlit as st



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
st.markdown("""
                <h2 style="border-radius:30px;text-align:center;background:cyan">AI-Based Cyber Attack Detection and Classification System</h2>
            
                """
                ,unsafe_allow_html=True)
col_1,col_2,col_3=st.columns([1,3,1])
with col_2:
      st.image("imge.jpg",width=500)

with st.container(border=True):

    st.markdown("""
<div style="background:#9CA3AF;font-size:20px;padding:20px;border-radius:25px;">
<div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">
<h3 style="color:blue">1.System Overview<h3>
<p><i>
    An intelligent system that leverages Machine Learning
    techniques to detect and classify cyber attacks by analyzing network
    traffic data. The system is designed to help cybersecurity
    professionals identify threats quickly and accurately
    </i></p>
</div>
<div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">

<h3 style="color:blue">2.Project Objectives<h3>   
            <ul style="font-size:20px;padding:6px;border-radius:25px"> <i>            
                <li> Detect cyber attacks.</li>
                <li>Classify attack types.</li>
                <li>Display prediction confidence.</li>
                <li>Provide a user-friendly interface.</li>
                <li>Improve threat detection and response speed.</li>
                </i>
            </ul>
</div>
<div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">

<h3 style="color:blue">3.Model Information:<h3>   
        <ul style="font-size:20px;padding:6px;border-radius:25px">
                <i>
            <li>Algorithm :Random Forest</li>
            <li>Dataset:UNSW-NB15</li>
            <li>Number of Features : 13 Feature</li>
            <li>Number of Attack Categories : 10 Categories</li>
                </i>
                </ul>
</div>  
<div style="background:white;font-size:20px;padding:20px;border-radius:25px;margin:10px 0">
<h3 style="color:blue">4.Quick Statistics (Dashboard):</h3>
<table style="background-color:white;text-algin:center;margin:0px 50px;width:80%">
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
                
</div>
</div>  
                """,unsafe_allow_html=True)

    st.write("")
    if st.button("🔍 Prediction",width="stretch"):
        st.switch_page("pages/Prediction.py")

        
st.markdown("""
                
    <div style="background-color:white;border:2px dashed;margin:50px 0;padding:10px;border-radius:30px;text-algin:center">
    <h4> Developed by:</h4>
                
    <b>Student: Anas Mohammed Abd ALijalyl Saeed</b>
    <p>
        Department of Artificial Intelligence
        University of Taiz
                <p style="text-align:center;background-color:black;color:white">© 2026</p>
    </p>

    </div>
 
    """,unsafe_allow_html=True)


