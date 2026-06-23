import streamlit as st
import random
import time
import base64


st.set_page_config(
    page_title="Đua Ngựa",
    layout="wide"
)

st.title("🐎 GAME ĐUA NGỰA")


# ======= ẢNH NGỰA =======
def load_img(file):
    with open(file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return data


horse_img = load_img("ngua.png")


# ======= CSS =======

st.markdown("""
<style>

.duongdua{
    height:90px;
    border-bottom:2px dashed #aaa;
    position:relative;
}


.horse{
    position:absolute;
    top:10px;
    animation: chay .25s infinite alternate;
}


@keyframes chay {
    from {
        transform: translateY(0px) rotate(-2deg);
    }
    to {
        transform: translateY(-6px) rotate(2deg);
    }
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
    right:10px;
    top:35px;
    color:red;
    font-weight:bold;
}


</style>
""", unsafe_allow_html=True)


if "vitri" not in st.session_state:
    st.session_state.vitri = [0,0,0,0,0]


khung = st.empty()


def ve_duong():
    
    html = ""

    for i,x in enumerate(st.session_state.vitri):

        html += f"""

        <div class="duongdua">

        <div class="start">
        Xuất phát
        </div>


        <div class="horse"
        style="left:{x}%">

        <img src="data:image/png;base64,{horse_img}"
        width="120">

        </div>


        <div class="finish">
        Đích 🏆
        </div>


        </div>

        """

    khung.markdown(
        html,
        unsafe_allow_html=True
    )



ve_duong()



if st.button("🚩 BẮT ĐẦU ĐUA"):

    st.session_state.vitri=[
        0,0,0,0,0
    ]

    winner=None

    while winner is None:

        for i in range(5):

            st.session_state.vitri[i]+=random.randint(1,5)

            if st.session_state.vitri[i]>=85:
                winner=i+1
                break


        ve_duong()

        time.sleep(0.15)


    st.success(
        f"🏆 Ngựa số {winner} chiến thắng"
    )