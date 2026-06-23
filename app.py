import streamlit as st
import time
import random
import base64
import os

# Cấu hình trang
st.set_page_config(page_title="Đua Ngựa Vui Vẻ", layout="wide")

st.title("🏇 Giải Đua Ngựa Vô Địch")

# 1. Đọc ảnh và chuyển sang định dạng base64
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        return None

img_path = "ngua.gif"
img_base64 = get_image_base64(img_path)

# CSS tạo sân đua chuyên nghiệp
st.markdown("""
    <style>
    .track { 
        background: linear-gradient(to bottom, #4CAF50 0%, #2e7d32 100%); 
        height: 450px; 
        border-bottom: 10px solid #5d4037; 
        padding: 20px; 
        position: relative; 
        border-radius: 10px;
        overflow: hidden;
    }
    .finish-line { 
        position: absolute; 
        right: 20px; 
        top: 0; 
        bottom: 0; 
        width: 10px; 
        background: white; 
        border-left: 2px dashed #000; 
    }
    .horse { 
        position: absolute; 
        width: 80px; 
        transition: left 0.1s linear; 
    }
    </style>
""", unsafe_allow_html=True)

# 2. Logic trò chơi
if st.button("🏁 Bắt đầu cuộc đua!"):
    if img_base64 is None:
        st.error(f"Không tìm thấy file '{img_path}'. Hãy kiểm tra xem file đã nằm cùng thư mục với app.py chưa!")
    else:
        # Khởi tạo vị trí 5 con ngựa
        positions = [0] * 5
        track_width = 750
        
        # Tạo container chứa sân đua
        track_container = st.empty()
        
        winner = -1
        
        # Vòng lặp đua
        while max(positions) < track_width:
            # Tạo HTML cho sân đua và các con ngựa
            html_content = '<div class="track"><div class="finish-line"></div>'
            for i in range(5):
                # Cập nhật vị trí ngẫu nhiên
                positions[i] += random.randint(5, 15)
                # Đảm bảo không vượt quá vạch đích
                if positions[i] > track_width: positions[i] = track_width
                
                html_content += f'<img src="data:image/gif;base64,{img_base64}" class="horse" style="left: {positions[i]}px; top: {i*80 + 20}px;">'
            html_content += '</div>'
            
            # Cập nhật hiển thị
            track_container.markdown(html_content, unsafe_allow_html=True)
            
            # Kiểm tra người thắng cuộc
            for i in range(5):
                if positions[i] >= track_width and winner == -1:
                    winner = i + 1
            
            time.sleep(0.05)
            
        st.balloons()
        st.success(f"🎉 Chúc mừng ngựa số {winner} đã về đích đầu tiên!")
else:
    # Giao diện sân đua tĩnh khi chưa chạy
    st.markdown('<div class="track"><div class="finish-line"></div></div>', unsafe_allow_html=True)
