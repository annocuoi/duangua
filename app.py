import streamlit as st
import random
import time
import base64
import streamlit.components.v1 as components


# =========================
# CÀI ĐẶT TRANG
# =========================

st.set_page_config(
    page_title="Đua Ngựa",
    layout="wide"
)

st.title("🐎 GAME ĐUA NGỰA")


# =========================
# LOAD GIF NGỰA
# =========================

def load_file(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()


ngua = load_file("ngua_tu_video.gif")


# =========================
# CSS GAME
# =========================

st.markdown(
"""
<style>

.duongdua{
    width:100%;
    height:100px;
    border-bottom:2px dashed #999;
    position:relative;
    overflow:hidden;
}


.start{
    position:absolute;
    left:0;
    top:40px;
    color:green;
    font-size:18px;
    font-weight:bold;
}


.finish{
    position:absolute;
    right:20px;
    top:40px;
    color:red;
    font-size:18px;
    font-weight:bold;
}


.horse{
    position:absolute;
    top:10px;
}


</style>
""",
unsafe_allow_html=True
)


# =========================
# BIẾN GAME
# =========================

if "vitri" not in st.session_state:
    st.session_state.vitri = [
        0,0,0,0,0
    ]

# =========================
# VẼ ĐƯỜNG ĐUA
# =========================

def ve_game():

    html = """
    <style>

    .duongdua{
        width:100%;
        height:100px;
        border-bottom:2px dashed gray;
        position:relative;
    }

    .start{
        position:absolute;
        left:0;
        top:35px;
        color:green;
        font-weight:bold;
    }

    .finish{
        position:absolute;
        right:20px;
        top:35px;
        color:red;
        font-weight:bold;
    }

    .horse{
        position:absolute;
        top:10px;
    }

    </style>
    """


    for i in range(5):

        html += f"""

        <div class="duongdua">

            <div class="start">
            Xuất phát
            </div>


            <div class="horse"
            style="left:{st.session_state.vitri[i]}%">

                <img
                src="data:image/gif;base64,{ngua}"
                width="130">

            </div>


            <div class="finish">
            Đích 🏆
            </div>


        </div>

        """


    components.html(
        html,
        height=600
    )

# =========================
# NÚT CHẠY
# =========================


if st.button("🚩 BẮT ĐẦU ĐUA"):


    st.session_state.vitri=[
        0,0,0,0,0
    ]

    thang = None


    while thang is None:


        for i in range(5):

            buoc = random.randint(
                1,5
            )

            st.session_state.vitri[i]+=buoc


            if st.session_state.vitri[i] >= 88:

                thang = i+1

                break


        ve_game()

        time.sleep(0.12)



    st.balloons()

    st.success(
        f"🏆 NGỰA SỐ {thang} CHIẾN THẮNG"
    )
