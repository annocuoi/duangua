import streamlit as st
import time
import random
import math

st.title("🐔 Đấu Trường Đá Gà")

# CSS tạo sân đấu hình tròn
st.markdown("""
    <style>
    .arena {
        width: 400px; height: 400px; border: 5px solid #5d4037;
        border-radius: 50%; background-color: #f1f8e9;
        position: relative; margin: 0 auto;
    }
    .chicken {
        width: 30px; height: 30px; border-radius: 50%;
        position: absolute; transition: all 0.1s linear;
    }
    </style>
""", unsafe_allow_html=True)

if st.button("Bắt đầu trận đấu!"):
    # Vị trí ban đầu
    chickens = [{'x': 100, 'y': 200, 'color': 'red', 'dx': 5, 'dy': 5},
                {'x': 300, 'y': 200, 'color': 'blue', 'dx': -5, 'dy': -5}]
    
    arena_placeholder = st.empty()
    start_time = time.time()
    
    while time.time() - start_time < 30:
        html = '<div class="arena">'
        
        for c in chickens:
            # Di chuyển
            c['x'] += c['dx'] + random.randint(-2, 2)
            c['y'] += c['dy'] + random.randint(-2, 2)
            
            # Va chạm tường (sân tròn)
            dist_from_center = math.sqrt((c['x']-200)**2 + (c['y']-200)**2)
            if dist_from_center > 185:
                c['dx'] *= -1
                c['dy'] *= -1
            
            html += f'<div class="chicken" style="left:{c["x"]}px; top:{c["y"]}px; background-color:{c["color"]};"></div>'
            
        html += '</div>'
        arena_placeholder.markdown(html, unsafe_allow_html=True)
        time.sleep(0.05)
        
    # Kết quả sau 30s
    winner = random.choice(["Gà Đỏ", "Gà Xanh"])
    st.balloons()
    st.success(f"Trận đấu kết thúc! {winner} đã giành chiến thắng!")
