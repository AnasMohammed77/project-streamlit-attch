import streamlit as st
import requests
st.markdown(
    """
<style>

div.stButton>button{
background-color:limegreen;
border:non ;
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
<h2 style="border-radius:30px;text-align:center;background:cyan">Cyber Attack Prediction</h2>

""",unsafe_allow_html=True)

col_1,col_2,col_3=st.columns([1,3,1])
with col_2:
        st.image("imge.jpg",width=500)
with st.container(border=True):


    st.markdown("""
<b>
Enter the network traffic features below to analyze the connection 
and predict whether it is normal or malicious.
</b>
                """
                ,unsafe_allow_html=True)


    col1,col2,col3,col4=st.columns(4)
    with col1:
        service=st.text_input("service")
        sbytes=st.number_input("sbytes",value=0)
        dbytes=st.number_input("dbytes",value=0)
    with col2:
        sttl=st.number_input("sttl",value=0)
        dttl=st.number_input("dttl",value=0)
        sload=st.number_input("sload",value=0)
    


    with col3:
        dload=st.number_input("dload",value=0)    

        smean=st.number_input("smean",value=0)
        dmean=st.number_input("dmean",value=0)
    with col4:
        ct_srv_src=st.number_input("ct_srv_src",value=0)
        ct_state_ttl=st.number_input("ct_state_ttl,value=0",value=0)
        ct_dst_src_ltm=st.number_input("ct_dst_src_ltm",value=0)
    with col2:

        ct_srv_dst=st.number_input("ct_srv_dst",value=0)
    try:
        if st.button("🔍 Analyze Network Traffic",width="stretch"):
                data={
                    "service":service,
                    "sbytes":sbytes,
                    "dbytes":dbytes,
                    "sttl":sttl,
                    "dttl":dttl,
                    "sload":sload,
                    "dload":dload,
                    "smean":smean,
                    "dmean":dmean,
                    "ct_srv_src":ct_srv_src,
                    "ct_state_ttl":ct_state_ttl,
                    "ct_dst_src_ltm":ct_dst_src_ltm,
                    "ct_srv_dst":ct_srv_dst

                }
                response=requests.post(
                    "http://127.0.0.1:8000/predict",json=data
                )
                result=response.json()
                if result["attach"]=="Normal":
                    st.success(f"🟢 Normal Traffic")
                    st.success(f" Attack Type :{result["attach"]}")
                if result["attach"]!="Normal":
                    st.error(f"🔴 A potential cyber attack has been detected.")
                    st.success(f" Attack Type :{result["attach"]}")
                    
                st.info((f"Prediction Confidence : {result["probability"]} %"))
                st.info((f"Prediction Time : {result["total_time"]*1000} ms "))
    except  Exception as e :
                st.error(f"An erorr occurred during data processing.")

             

    st.markdown("""
                <div style="border:2px dashed;margin:50px 0;padding:10px;border-radius:30px">
    <h4> Developed by:</h4>
                
    <b>Student: Anas Mohammed Abd ALijalyl Saeed</b>
    <p>
        Department of Artificial Intelligence
        University of Taiz
                <p style="text-align:center;background-color:black;color:white">© 2026</p>
    </p>

    </div>
    """,unsafe_allow_html=True)

