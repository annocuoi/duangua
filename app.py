import streamlit as st
import time
import random

st.set_page_config(page_title="Đua Ngựa Vui Vẻ", layout="wide")

st.title("🏇 Trò Chơi Đua Ngựa")

# CSS để tạo sân đua chuyên nghiệp
st.markdown("""
    <style>
    .track { background-color: #2d5a27; height: 400px; border-bottom: 5px solid #d2b48c; padding: 20px; position: relative; }
    .horse { position: absolute; width: 80px; transition: left 0.3s linear; }
    .finish-line { position: absolute; right: 20px; top: 0; bottom: 0; width: 5px; background: white; }
    </style>
""", unsafe_allow_html=True)

if st.button("Bắt đầu đua!"):
    # Vị trí của 5 con ngựa
    positions = [0] * 5
    track_width = 800
    
    # Tạo container cho sân đua
    track_container = st.container()
    with track_container:
        st.markdown('<div class="track">', unsafe_allow_html=True)
        # Hiển thị vạch đích
        st.markdown('<div class="finish-line"></div>', unsafe_allow_html=True)
        
        # Placeholder cho ngựa
        horse_placeholders = [st.empty() for _ in range(5)]
        
        winner = -1
        while max(positions) < track_width:
            for i in range(5):
                # Random tốc độ: mỗi bước tiến từ 5 đến 20 pixel
                positions[i] += random.randint(5, 20)
                
                # Hiển thị ảnh ngựa (cần file 'ngua.gif' trong cùng thư mục)
                horse_placeholders[i].markdown(
                    f'<img src="data:image/gif;base64,{open("ngua.gif", "rb").read().hex()}" '
                    f'class="horse" style="left: {positions[i]}px; top: {i*70 + 20}px;">', 
                    unsafe_allow_html=True
                )
                
                if positions[i] >= track_width and winner == -1:
                    winner = i + 1
            
            time.sleep(0.1)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.success(f"🎉 Chúc mừng ngựa số {winner} đã về đích đầu tiên!")
