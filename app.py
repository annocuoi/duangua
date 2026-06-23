import streamlit as st
import time
import random
import base64

st.set_page_config(page_title="Đua Ngựa Vui Vẻ", layout="wide")
st.title("🏇 Giải Đua Ngựa - Camera Cận Cảnh")

# 1. Hàm load ảnh ngựa
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

img_path = "ngua.gif" # Đảm bảo file ngua.gif vẫn ở cùng thư mục
img_base64 = get_image_base64(img_path)

# 2. CSS thiết lập Camera Box và Track
st.markdown("""
    <style>
    /* Khung camera cố định, cắt bỏ những phần thừa khi phóng to */
    .camera-box {
        width: 100%;
        height: 450px;
        overflow: hidden; 
        border-radius: 10px;
        border: 5px solid #333;
        position: relative;
    }
    
    /* Sân đua sẽ được phóng to bên trong khung camera */
    .track { 
        background: linear-gradient(to bottom, #4CAF50 0%, #2e7d32 100%); 
        height: 100%; 
        width: 100%;
        position: relative; 
        /* Tỉ lệ phóng to (zoom in 1.5 lần) */
        transform: scale(1.5); 
        transition: transform-origin 0.1s linear; /* Hiệu ứng camera lia mượt */
    }
    
    .finish-line { 
        position: absolute; right: 40px; top: 0; bottom: 0; 
        width: 10px; background: white; border-left: 2px dashed #000; 
    }
    
    .horse { 
        position: absolute; width: 60px; 
        transition: left 0.1s linear; 
    }
    </style>
""", unsafe_allow_html=True)

if st.button("🏁 Bắt đầu cuộc đua!"):
    if img_base64 is None:
        st.error(f"Không tìm thấy file '{img_path}'.")
    else:
        positions = [0] * 5
        track_width = 800
        track_container = st.empty()
        winner = -1
        
        while max(positions) < track_width:
            # 1. Tính toán vị trí của con ngựa dẫn đầu
            lead_horse_pos = max(positions)
            
            # 2. Tính % trục X để lia camera theo ngựa dẫn đầu
            # Chia cho track_width để lấy tỉ lệ % (từ 0% đến 100%)
            camera_x_percent = (lead_horse_pos / track_width) * 100
            
            # Giới hạn camera không trôi ra khỏi lề trái (bắt đầu từ 20%)
            camera_x_percent = max(20, camera_x_percent) 
            
            # 3. Tạo HTML: Đưa tọa độ vào transform-origin của CSS
            html_content = f'<div class="camera-box">'
            html_content += f'<div class="track" style="transform-origin: {camera_x_percent}% 50%;">'
            html_content += '<div class="finish-line"></div>'
            
            for i in range(5):
                # Random tốc độ chạy
                positions[i] += random.randint(5, 20)
                if positions[i] > track_width: 
                    positions[i] = track_width
                
                # Render từng con ngựa
                html_content += f'<img src="data:image/gif;base64,{img_base64}" class="horse" style="left: {positions[i]}px; top: {i*80 + 20}px;">'
                
            html_content += '</div></div>'
            
            # 4. Hiển thị lên Streamlit
            track_container.markdown(html_content, unsafe_allow_html=True)
            
            # Kiểm tra ngựa chiến thắng
            for i in range(5):
                if positions[i] >= track_width and winner == -1:
                    winner = i + 1
            
            time.sleep(0.05)
            
        st.balloons()
        st.success(f"🎉 Chúc mừng ngựa số {winner} đã về đích đầu tiên!")
else:
    # Giao diện tĩnh lúc ban đầu
    st.markdown('''
        <div class="camera-box">
            <div class="track" style="transform-origin: 20% 50%;">
                <div class="finish-line"></div>
            </div>
        </div>
    ''', unsafe_allow_html=True)
